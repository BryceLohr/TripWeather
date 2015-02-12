from django.db import models

class Airport(models.Model):
    """
    Represents the OpenFlights.org Airports database. See
    http://openflights.org/data.html
    """
    name = models.CharField(max_length=75)
    city = models.CharField(max_length=75)
    country = models.CharField(max_length=75)
    iata_faa = models.CharField(max_length=3, db_index=True, null=True, blank=True)
    icao = models.CharField(max_length=4, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    altitude = models.IntegerField(help_text="In feet")
    timezone = models.DecimalField(max_digits=3, decimal_places=1, help_text="Offset from UTC in hours")
    dst_code = models.CharField(max_length=1)
    tz_name = models.CharField(max_length=75, help_text="Name from the Olson timezone database")


