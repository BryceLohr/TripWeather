# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routeforecast',
            name='query_json',
        ),
        migrations.AddField(
            model_name='routeforecast',
            name='arrive_latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routeforecast',
            name='arrive_longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routeforecast',
            name='depart_latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routeforecast',
            name='depart_longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routeforecast',
            name='depart_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 27, 1, 16, 38, 907686, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routeforecast',
            name='planned_speed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routeforecast',
            name='report_interval',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
