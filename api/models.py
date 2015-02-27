from django.db import models


class FlightPlan(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    depart_latitude = models.FloatField()
    depart_longitude = models.FloatField()
    arrive_latitude = models.FloatField()
    arrive_longitude = models.FloatField()
    depart_time = models.DateTimeField()
    planned_speed = models.IntegerField()
    report_interval = models.IntegerField()


class WeatherReport(models.Model):
    flight_plan = models.ForeignKey(FlightPlan)
    # Field names violate Django convention to match those from the WeatherSouce API
    timestamp = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    cldCvr = models.FloatField(null=True)
    precip = models.FloatField(null=True)
    precipProb = models.FloatField(null=True)
    sfcPres = models.FloatField(null=True)
    snowfall = models.FloatField(null=True)
    snowfallProb = models.FloatField(null=True)
    spcHum = models.FloatField(null=True)
    temp = models.FloatField(null=True)
    windSpd = models.FloatField(null=True)
    windDir = models.FloatField(null=True)

