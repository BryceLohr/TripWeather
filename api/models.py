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

    def __unicode__(self):
        return u"Flight Plan {0}".format(self.id)


class WeatherReport(models.Model):
    flight_plan = models.ForeignKey(FlightPlan)
    # Field names violate Django convention to match those from the WeatherSouce API
    timestamp = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    cldCvr = models.FloatField('cloud cover', null=True, help_text="Percentage")
    precip = models.FloatField('precipitation', null=True, help_text="In inches")
    precipProb = models.FloatField('precipitation chance', null=True, help_text="Percentage")
    sfcPres = models.FloatField('surface pressure', null=True, help_text="In millibars")
    snowfall = models.FloatField('snowfall', null=True, help_text="In inches")
    snowfallProb = models.FloatField('snowfall chance', null=True, help_text="Percentage")
    spcHum = models.FloatField('specific humidity', null=True, help_text="In grams per kilogram")
    temp = models.FloatField('temperature', null=True, help_text="In degrees Fahrenheit")
    windSpd = models.FloatField('wind speed', null=True, help_text="In miles per hour")
    windDir = models.FloatField('wind direction', null=True, help_text="In clockwise compass degrees; 360 is North; 0 is no wind")

    def __unicode__(self):
        return u"Weather Report {0}".format(self.id)
