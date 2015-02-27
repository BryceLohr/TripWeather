# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_more_weather_fields'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RouteForecast',
            new_name='FlightPlan',
        ),
        migrations.RenameModel(
            old_name='RouteForecastWeather',
            new_name='WeatherReports',
        ),
        migrations.RenameField(
            model_name='weatherreports',
            old_name='route_forecast',
            new_name='flight_plan',
        ),
    ]
