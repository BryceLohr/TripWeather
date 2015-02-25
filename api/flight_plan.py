import calendar
from datetime import datetime, timedelta
import math
import re

from django import forms
from django.conf import settings
from pysal.cg import sphere
import pytz
import requests

from ui.models import Airport


class FlightPlanForm(forms.Form):
    depart_location = forms.CharField(max_length=10)
    arrive_location = forms.CharField(max_length=10)
    depart_time = forms.DateTimeField(error_messages={'invalid': "Date time should be in ISO 8601 format"})
    planned_speed = forms.IntegerField(max_value=761, min_value=1, help_text="In miles per hour")
    report_interval = forms.IntegerField(max_value=168, min_value=1, help_text="In hours")

    def validate_location(self, initial_value):
        try:
            if re.match(r'^[a-zA-Z]{3}$', initial_value):
                airport = Airport.objects.get(iata_faa=initial_value.upper())
                return (float(airport.latitude), float(airport.longitude))

            else:
                lat, lon = initial_value.split(',')
                lat = float(lat)
                lon = float(lon)
                if lat < -90.0 or lat > 90.0:
                    raise forms.ValidationError("Latitude must be between -90.0 and 90.0", code="invalid")
                if lon < -180.0 or lon > 180.0:
                    raise forms.ValidationError("longitude must be between -180.0 and 180.0", code="invalid")
                return (lat, lon)

        except (ValueError, Airport.DoesNotExist):
            raise forms.ValidationError("Location must be a 3-letter airport code or a lat/long pair separated by a comma", code="invalid")

    def clean_depart_location(self):
        return self.validate_location(self.cleaned_data['depart_location'])

    def clean_arrive_location(self):
        return self.validate_location(self.cleaned_data['arrive_location'])


def build_flight_plan(depart, arrive, utc_depart_time, mph, interval):
    # Swap lat/lon around for PySAL
    depart = (depart[1], depart[0])
    arrive = (arrive[1], arrive[0])

    miles = sphere.arcdist(depart, arrive, sphere.RADIUS_EARTH_MILES)
    hours = miles / float(mph)
    utc_arrive_time = (utc_depart_time + timedelta(hours=hours))
    reports = int(math.floor(hours / min(interval, hours)))

    plan = []
    for i in range(reports):
        coords = sphere.geointerpolate(depart, arrive, (i*interval)/float(hours))
        utc_report_time = utc_depart_time + timedelta(hours=(i*interval))
        local_report_time = get_local_time(coords[1], coords[0], utc_report_time)

        plan.append({
            'intervalId': i,
            'latitude': coords[1],
            'longitude': coords[0],
            'timestamp': repr(local_report_time),
        })

    plan.append({
        'intervalId': reports,
        'latitude': arrive[1],
        'longitude': arrive[0],
        'timestamp': repr(get_local_time(arrive[1], arrive[0], utc_arrive_time)),
    })

    return plan


def get_local_time(latitude, longitude, utc_datetime):
    tz_api_url = "https://maps.googleapis.com/maps/api/timezone/json"
    api_params = {
        'location': "{0},{1}".format(latitude, longitude),
        'timestamp': calendar.timegm(utc_datetime.timetuple()),
        'api_key': settings.GOOGLE_API_KEY,
    }

    tz_data = requests.get(tz_api_url, params=api_params).json()
    local_timezone = pytz.timezone(tz_data['timeZoneId'])

    return local_timezone.normalize(utc_datetime.astimezone(local_timezone))
