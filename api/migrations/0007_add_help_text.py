# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_nullable_weather_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherreport',
            name='cldCvr',
            field=models.FloatField(help_text=b'Percentage', null=True, verbose_name=b'cloud cover'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='precip',
            field=models.FloatField(help_text=b'In inches', null=True, verbose_name=b'precipitation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='precipProb',
            field=models.FloatField(help_text=b'Percentage', null=True, verbose_name=b'precipitation chance'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='sfcPres',
            field=models.FloatField(help_text=b'In millibars', null=True, verbose_name=b'surface pressure'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='snowfall',
            field=models.FloatField(help_text=b'In inches', null=True, verbose_name=b'snowfall'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='snowfallProb',
            field=models.FloatField(help_text=b'Percentage', null=True, verbose_name=b'snowfall chance'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='spcHum',
            field=models.FloatField(help_text=b'In grams per kilogram', null=True, verbose_name=b'specific humidity'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='temp',
            field=models.FloatField(help_text=b'In degrees Fahrenheit', null=True, verbose_name=b'temperature'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='windDir',
            field=models.FloatField(help_text=b'In clockwise compass degrees; 360 is North; 0 is no wind', null=True, verbose_name=b'wind direction'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='windSpd',
            field=models.FloatField(help_text=b'In miles per hour', null=True, verbose_name=b'wind speed'),
            preserve_default=True,
        ),
    ]
