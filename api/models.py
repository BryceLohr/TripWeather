from django.db import models


class RouteForecast(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    query_json = models.TextField()  # Clear violation of 1NF, but sub-values are not individually queried or updated.


class RouteForecastWeather(models.Model):
    route_forecast = models.ForeignKey(RouteForecast)
    # Field names violate Django convention to match those from the WeatherSouce API
    timestamp = models.DateTimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    precip = models.DecimalField(max_digits=5, decimal_places=2)
    precipProb = models.DecimalField(max_digits=5, decimal_places=2)
    sfcPres = models.DecimalField(max_digits=5, decimal_places=1)
    spcHum = models.DecimalField(max_digits=5, decimal_places=2)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    windSpd = models.DecimalField(max_digits=5, decimal_places=2)
    windDir = models.DecimalField(max_digits=5, decimal_places=2)

