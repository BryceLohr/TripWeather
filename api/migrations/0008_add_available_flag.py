# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_add_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherreport',
            name='available',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
