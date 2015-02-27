# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_add_flight_plan_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='routeforecastweather',
            name='cldCvr',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routeforecastweather',
            name='snowfall',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routeforecastweather',
            name='snowfallProb',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='routeforecastweather',
            name='latitude',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='routeforecastweather',
            name='longitude',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='routeforecastweather',
            name='precip',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='routeforecastweather',
            name='precipProb',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='routeforecastweather',
            name='sfcPres',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='routeforecastweather',
            name='spcHum',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='routeforecastweather',
            name='temp',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='routeforecastweather',
            name='windDir',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='routeforecastweather',
            name='windSpd',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
