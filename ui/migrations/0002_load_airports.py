# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

from django.db import models, migrations
from django.conf import settings


def load_airports_from_csv(apps, schema_editor):
    in_file = settings.BASE_DIR + '/ui/fixtures/airports.dat'
    Airport = apps.get_model("ui", "Airport")

    with open(in_file, 'rb') as csvfile:
        for i, row in enumerate(csv.reader(csvfile, dialect='excel')):
            if i < 3:
                continue
            data = [v if v != b'\\N' else '' for v in row]

            airport = Airport()
            airport.id = int(data[0])
            airport.name = data[1]
            airport.city = data[2]
            airport.country = data[3]
            airport.iata_faa = data[4] if data[4] else None
            airport.icao = data[5] if data[5] else None
            airport.latitude = float(data[6])
            airport.longitude = float(data[7])
            airport.altitude = int(data[8])
            airport.timezone = float(data[9])
            airport.dst_code = data[10]
            airport.tz_name = data[11]
            airport.save()

def unload_airports(apps, schema_editor):
    Airport = apps.get_model("ui", "Airport")
    Airport.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_airports_from_csv, unload_airports)
    ]
