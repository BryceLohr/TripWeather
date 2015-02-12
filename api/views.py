import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from restless.views import Endpoint

from api import flight_plan


class FlightPlan(Endpoint):
    def post(self, request):
        try:
            decoded = json.loads(request.data)
            form = flight_plan.FlightPlanForm(decoded)
            if form.is_valid():
                return flight_plan.build_flight_plan(
                    form.cleaned_data['depart_location'],
                    form.cleaned_data['arrive_location'],
                    form.cleaned_data['depart_time'],
                    form.cleaned_data['planned_speed'],
                    form.cleaned_data['report_interval'])
            else:
                return HttpResponse(form.errors.as_json(), status=400, content_type="text/json")
        except ValueError:
            return HttpResponse("Invalid JSON document", status=415)


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
