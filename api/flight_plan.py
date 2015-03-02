import calendar
from datetime import datetime, timedelta
import math
import re

from django import forms
from django.conf import settings
from django.db import transaction
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from pysal.cg import sphere
import pytz
import requests

from ui.models import Airport
from api.models import FlightPlan, WeatherReport


class FlightPlanForm(forms.ModelForm):
    depart_location = forms.CharField(max_length=10)
    arrive_location = forms.CharField(max_length=10)
    depart_time = forms.DateTimeField(error_messages={'invalid': "Date time should be in ISO 8601 format"})
    planned_speed = forms.IntegerField(max_value=761, min_value=1, help_text="In miles per hour")
    report_interval = forms.IntegerField(max_value=168, min_value=1, help_text="In hours")

    class Meta:
        model = FlightPlan
        fields = ['depart_time', 'planned_speed', 'report_interval']

    def _validate_location(self, initial_value):
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
        latlon = self._validate_location(self.cleaned_data['depart_location'])
        self.instance.depart_latitude = latlon[0]
        self.instance.depart_longitude = latlon[1]
        return latlon

    def clean_arrive_location(self):
        latlon = self._validate_location(self.cleaned_data['arrive_location'])
        self.instance.arrive_latitude = latlon[0]
        self.instance.arrive_longitude = latlon[1]
        return latlon

    def clean(self):
        # The depart_time is assigned the UTC time zone because the default time
        # zone is set to UTC in settings. We need to interpret the given time as
        # the local time of the depart_location, not as UTC. Then we can get the
        # UTC equivalent of the local depart time.
        local_timezone = get_local_timezone(self.instance.depart_latitude, self.instance.depart_longitude, self.cleaned_data['depart_time'])
        local_depart_time = self.cleaned_data['depart_time'].replace(tzinfo=local_timezone)
        utc_depart_time = pytz.utc.normalize(local_depart_time.astimezone(pytz.utc))

        # Limit depart_time to between the start of this hour and 7 days from now
        this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
        plus_7days = this_hour + timedelta(days=7)

        if utc_depart_time < this_hour or utc_depart_time > plus_7days:
            self.add_error('depart_time', forms.ValidationError("Depart time must be between the start of this hour and 7 days from now", code='invalid'))
        else:
            self.instance.depart_time = utc_depart_time


def build_flight_plan(flight_plan_form):
    new_flight_plan = flight_plan_form.save(commit=False)

    # PySAL wants lat/lon as lon/lat
    depart = (new_flight_plan.depart_longitude, new_flight_plan.depart_latitude)
    arrive = (new_flight_plan.arrive_longitude, new_flight_plan.arrive_latitude)
    interval = new_flight_plan.report_interval
    utc_depart_time = new_flight_plan.depart_time

    miles = sphere.arcdist(depart, arrive, sphere.RADIUS_EARTH_MILES)
    hours = miles / float(new_flight_plan.planned_speed)
    utc_arrive_time = utc_depart_time + timedelta(hours=hours)
    reports = min(int(math.floor(hours / min(interval, hours))), 50)

    # Provides the point to center the map on
    midpoint = sphere.geointerpolate(depart, arrive, 0.5)
    new_flight_plan.midpoint_latitude = midpoint[1]
    new_flight_plan.midpoint_longitude = midpoint[0]

    weather_reports = []
    for i in range(reports):
        coords = sphere.geointerpolate(depart, arrive, (i*interval)/float(hours))
        utc_report_time = utc_depart_time + timedelta(hours=(i*interval))
        weather_reports.append(
            build_weather_report(coords[1], coords[0], utc_report_time)
        )

    weather_reports.append(
        build_weather_report(arrive[1], arrive[0], utc_arrive_time)
    )

    return (new_flight_plan, weather_reports)

def build_weather_report(latitude, longitude, utc_report_time):
    local_timezone = get_local_timezone(latitude, longitude, utc_report_time)
    local_report_time = local_timezone.normalize(utc_report_time.astimezone(local_timezone))
    local_forecast = get_forecast_for_location(latitude, longitude)

    try:
        weather_at_time = find_weather_for_time(local_forecast, local_report_time)
        weather_report = WeatherReport(
            timestamp=local_report_time,
            latitude=latitude,
            longitude=longitude,
            available=True,
            cldCvr=weather_at_time['cldCvr'],
            precip=weather_at_time['precip'],
            precipProb=weather_at_time['precipProb'],
            sfcPres=weather_at_time['sfcPres'],
            snowfall=weather_at_time['snowfall'],
            snowfallProb=weather_at_time['snowfallProb'],
            spcHum=weather_at_time['spcHum'],
            temp=weather_at_time['temp'],
            windSpd=weather_at_time['windSpd'],
            windDir=weather_at_time['windDir']
        )

        return weather_report

    except TimeNotInForecast:
        return WeatherReport(
            timestamp=local_report_time,
            latitude=latitude,
            longitude=longitude,
            available=False
        )

def get_local_timezone(latitude, longitude, utc_datetime):
    tz_api_url = "https://maps.googleapis.com/maps/api/timezone/json"
    api_params = {
        'location': "{0},{1}".format(latitude, longitude),
        'timestamp': calendar.timegm(utc_datetime.timetuple()),
        'api_key': settings.GOOGLE_API_KEY,
    }

    response = requests.get(tz_api_url, params=api_params)
    response.raise_for_status()
    tz_data = response.json()
    try:
        return pytz.timezone(response.json()['timeZoneId'])
    except KeyError:
        raise TimezoneLookupError()

def get_forecast_for_location(latitude, longitude):
    weather_api_url = "https://api.weathersource.com/v1/{api_key}/forecast.json".format(api_key=settings.WEATHERSOURCE_API_KEY)
    api_params = {
        'latitude_eq': latitude,
        'longitude_eq': longitude,
        'period': 'hour',
        'fields': 'latitude,longitude,timestamp,temp,precip,precipProb,snowfall,snowfallProb,windSpd,windDir,cldCvr,spcHum,sfcPres'
    }

    response = requests.get(weather_api_url, params=api_params)
    response.raise_for_status()
    return response.json()

def find_weather_for_time(forecast, timestamp):
    for weather in forecast:
        weather_time = parse_datetime(weather['timestamp'])
        # Truncate the given time to its current hour, since WeatherSource returns times on the hour
        target_time = timestamp.replace(minute=0, second=0, microsecond=0)
        if weather_time == target_time:
            return weather

    raise TimeNotInForecast("No weather forecast was found for time {0}".format(timestamp))


def persist(flight_plan, weather_list):
    with transaction.atomic():
        flight_plan.save()

        for weather in weather_list:
            weather.flight_plan = flight_plan
            weather.save()

    return flight_plan.id


def get_flight_plan(flight_plan_id):
    try:
        return FlightPlan.objects.get(pk=flight_plan_id)
    except (FlightPlan.NotFound, WeatherReport.NotFound) as e:
        raise NotFound(str(e))


class NotFound(Exception):
    pass

class TimeNotInForecast(Exception):
    pass

class TimezoneLookupError(Exception):
    pass

