import calendar
from datetime import datetime, timedelta
import math
import re

from django import forms
from django.conf import settings
from django.db import transaction
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


def build_flight_plan(flight_plan_form):
    new_flight_plan = flight_plan_form.save(commit=False)

    # PySAL wants lat/lon as lon/lat
    depart = (new_flight_plan.depart_longitude, new_flight_plan.depart_latitude)
    arrive = (new_flight_plan.arrive_longitude, new_flight_plan.arrive_latitude)
    utc_depart_time = new_flight_plan.depart_time
    interval = new_flight_plan.report_interval

    miles = sphere.arcdist(depart, arrive, sphere.RADIUS_EARTH_MILES)
    hours = miles / float(new_flight_plan.planned_speed)
    utc_arrive_time = utc_depart_time + timedelta(hours=hours)
    reports = int(math.floor(hours / min(interval, hours)))

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
    local_report_time = get_local_time(latitude, longitude, utc_report_time)
    local_forecast = get_forecast_for_location(latitude, longitude)

    try:
        weather_at_time = find_weather_for_time(local_forecast, local_report_time)
        weather_report = WeatherReport(
            timestamp=local_report_time,
            latitude=latitude,
            longitude=longitude,
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
        return None

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

def get_forecast_for_location(latitude, longitude):
    weather_api_url = "https://api.weathersource.com/v1/{api_key}/forecast.json".format(api_key=settings.WEATHERSOURCE_API_KEY)
    api_params = {
        'latitude_eq': latitude,
        'longitude_eq': longitude,
        'period': 'hour',
        'fields': 'latitude,longitude,timestamp,temp,precip,precipProb,snowfall,snowfallProb,windSpd,windDir,cldCvr,spcHum,sfcPres'
    }

    response = requests.get(weather_api_url, params=api_params)
    return response.json()

def find_weather_for_time(forecast, timestamp):
    for weather in forecast:
        weather_time = parse_datetime(weather['timestamp'])
        # Truncate the given time to its current hour, since WeatherSource returns times on the hour
        given_time = timestamp.replace(minute=0, second=0, microsecond=0)
        if weather_time == given_time:
            return weather

    raise TimeNotInForecast("No weather forecast was found for time {0}".format(timestamp))


class TimeNotInForecast(Exception):
    pass


def persist(flight_plan, weather_list):
    with transaction.atomic():
        flight_plan.save()

        for weather in weather_list:
            weather.flight_plan = flight_plan
            weather.save()

    return flight_plan.id


def get_weather_reports(flight_plan_id):
    try:
        return WeatherReport.objects.filter(flight_plan_id=flight_plan_id).order_by('id')
    except WeatherReport.NotFound as e:
        # Wrapping exception to keep storage implementation behind facade
        raise NotFound(str(e))


class NotFound(Exception):
    pass
