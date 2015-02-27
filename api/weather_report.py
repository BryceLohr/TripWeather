import json

from django import forms
from django.conf import settings
from django.forms.formsets import BaseFormSet
import requests

from api.models import RouteForecast, RouteForecastWeather


class RouteForm(forms.Form):
    latitude = forms.DecimalField(max_digits=9, min_value=-90.0, max_value=90.0)
    longitude = forms.DecimalField(max_digits=9, min_value=-180.0, max_value=180.0)
    timestamp = forms.DateTimeField(error_messages={'invalid': "Date time should be in ISO 8601 format"},
        input_formats=['%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S'])


class MultiForm(object):
    """
    Django's form sets would work in theory, but they have too many hard-coded
    assumptions about the structure of the input data to be re-used for a list
    of JSON objects.
    """
    def __init__(self, form_class, data):
        self.form_class = form_class
        self.data = data
        self.errors = []
        self.cleaned_data = []

    def is_valid(self):
        if len(self.data) < 1:
            raise ValidationError("At least one record is required.", code="invalid")

        for datum in self.data:
            form = self.form_class(datum)
            if not form.is_valid():
                # Hack to work around JSONEncoder's sometimes inability to deal with ValidationError objects
                self.errors.append(json.loads(form.errors.as_json()))
            else:
                self.cleaned_data.append(form.cleaned_data)

        return len(self.errors) == 0


def create(route):
    weather_list = []
    for point in route:
        weather = get_forecast_for_location(point['latitude'], point['longitude'])
        weather = find_weather_for_time(weather, point['timestamp'])
        weather_list.append(weather)

    return save_to_db(route, weather_list)

