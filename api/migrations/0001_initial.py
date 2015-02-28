# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RouteForecast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('query_json', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RouteForecastWeather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('precip', models.DecimalField(max_digits=5, decimal_places=2)),
                ('precipProb', models.DecimalField(max_digits=5, decimal_places=2)),
                ('sfcPres', models.DecimalField(max_digits=5, decimal_places=1)),
                ('spcHum', models.DecimalField(max_digits=5, decimal_places=2)),
                ('temp', models.DecimalField(max_digits=5, decimal_places=2)),
                ('windSpd', models.DecimalField(max_digits=5, decimal_places=2)),
                ('windDir', models.DecimalField(max_digits=5, decimal_places=2)),
                ('route_forecast', models.ForeignKey(to='api.RouteForecast')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
