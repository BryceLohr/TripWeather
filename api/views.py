from django.core.urlresolvers import reverse
from django.http import HttpResponse

from restless.views import Endpoint


class FlightPlan(Endpoint):
    def get(self, request):
        return [
            { 'intervalId': 0, 'latitude': 40.639751, 'longitude': -73.778925 },
            { 'intervalId': 1, 'latitude': 41.34843913707863, 'longitude': -79.19563578614297 },
            { 'intervalId': 2, 'latitude': 41.79828792276403, 'longitude': -84.7094528354295 },
            { 'intervalId': 3, 'latitude': 41.98152391306366, 'longitude': -90.27792457775081 },
            { 'intervalId': 4, 'latitude': 41.89490005922622, 'longitude': -95.85483831531833 },
            { 'intervalId': 5, 'latitude': 41.53995731818525, 'longitude': -101.39338776897682 },
            { 'intervalId': 6, 'latitude': 40.922899672836124, 'longitude': -106.84943687506541 },
            { 'intervalId': 7, 'latitude': 40.05410602614879, 'longitude': -112.18435700307927 },
            { 'intervalId': 8, 'latitude': 38.9473669863364, 'longitude': -117.36703748446496 },
            { 'intervalId': 9, 'latitude': 37.618972, 'longitude': -122.374889 },
        ]


class WeatherForRoute(Endpoint):
    def post(self, request):
        # Query WeatherSource for weather at given coordinates and time stamps
        # Create new RouteForecast to store results
        forecast_id = 1

        response = HttpResponse(status=201)
        response['Location'] = reverse('weather_detail', args=[forecast_id])

        return response


class WeatherForRouteDetail(Endpoint):
    def get(self, request, forecast_id):
        return [
            {
                "timestamp": "2015-02-08T16:00:00-05:00",
                "latitude": 36.096,
                "longitude": -80.2517,
                "precip": 0,
                "precipProb": 0,
                "sfcPres": 1011.4,
                "spcHum": 5.2,
                "temp": 66,
                "windSpd": 15,
                "windDir": 220
            },
            {
                "timestamp": "2015-02-08T17:00:00-05:00",
                "latitude": 36.096,
                "longitude": -80.2517,
                "precip": 0,
                "precipProb": 0,
                "sfcPres": 1011.4,
                "spcHum": 5.1,
                "temp": 64,
                "windSpd": 14,
                "windDir": 210
            },
            {
                "timestamp": "2015-02-08T18:00:00-05:00",
                "latitude": 36.096,
                "longitude": -80.2517,
                "precip": 0,
                "precipProb": 0,
                "sfcPres": 1011.6,
                "spcHum": 5.1,
                "temp": 62,
                "windSpd": 12,
                "windDir": 210
            },
            {
                "timestamp": "2015-02-08T19:00:00-05:00",
                "latitude": 36.096,
                "longitude": -80.2517,
                "precip": 0,
                "precipProb": 0,
                "sfcPres": 1011.8,
                "spcHum": 5.1,
                "temp": 58,
                "windSpd": 10,
                "windDir": 210
            },
            {
                "timestamp": "2015-02-08T20:00:00-05:00",
                "latitude": 36.096,
                "longitude": -80.2517,
                "precip": 0,
                "precipProb": 0,
                "sfcPres": 1012.2,
                "spcHum": 5.4,
                "temp": 56.9,
                "windSpd": 8,
                "windDir": 210
            },
            {
                "timestamp": "2015-02-08T21:00:00-05:00",
                "latitude": 36.096,
                "longitude": -80.2517,
                "precip": 0,
                "precipProb": 0,
                "sfcPres": 1012.3,
                "spcHum": 5.6,
                "temp": 55,
                "windSpd": 7,
                "windDir": 210
            },
            {
                "timestamp": "2015-02-08T22:00:00-05:00",
                "latitude": 36.096,
                "longitude": -80.2517,
                "precip": 0,
                "precipProb": 0,
                "sfcPres": 1012.5,
                "spcHum": 5.8,
                "temp": 53,
                "windSpd": 7,
                "windDir": 219.5
            },
            {
                "timestamp": "2015-02-08T23:00:00-05:00",
                "latitude": 36.096,
                "longitude": -80.2517,
                "precip": 0,
                "precipProb": 0,
                "sfcPres": 1012.5,
                "spcHum": 6,
                "temp": 52,
                "windSpd": 7,
                "windDir": 214.9
            },
            {
                "timestamp": "2015-02-09T00:00:00-05:00",
                "latitude": 36.096,
                "longitude": -80.2517,
                "precip": 0,
                "precipProb": 0,
                "sfcPres": 1012.4,
                "spcHum": 6.5,
                "temp": 52,
                "windSpd": 7,
                "windDir": 210
            },
            {
                "timestamp": "2015-02-09T01:00:00-05:00",
                "latitude": 36.096,
                "longitude": -80.2517,
                "precip": 0,
                "precipProb": 0,
                "sfcPres": 1012.2,
                "spcHum": 6.8,
                "temp": 51,
                "windSpd": 7,
                "windDir": 210
            }
        ]
