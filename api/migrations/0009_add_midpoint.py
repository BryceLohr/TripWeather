# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_add_available_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightplan',
            name='midpoint_latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flightplan',
            name='midpoint_longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
