# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_models'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WeatherReports',
            new_name='WeatherReport',
        ),
    ]
