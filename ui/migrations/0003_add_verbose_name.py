# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_load_airports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='iata_faa',
            field=models.CharField(db_index=True, max_length=3, null=True, verbose_name=b'airport code', blank=True),
            preserve_default=True,
        ),
    ]
