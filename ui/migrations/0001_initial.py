# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=75)),
                ('country', models.CharField(max_length=75)),
                ('iata_faa', models.CharField(db_index=True, max_length=3, null=True, blank=True)),
                ('icao', models.CharField(max_length=4, null=True, blank=True)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('altitude', models.IntegerField(help_text=b'In feet')),
                ('timezone', models.DecimalField(help_text=b'Offset from UTC in hours', max_digits=3, decimal_places=1)),
                ('dst_code', models.CharField(max_length=1)),
                ('tz_name', models.CharField(help_text=b'Name from the Olson timezone database', max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
