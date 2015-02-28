angular.module('WeatherData', [])
.factory('getWeatherAtCoords', function() {
  var weatherData = [
  {
    "intervalId": 0,
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
    "intervalId": 1,
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
    "intervalId": 2,
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
    "intervalId": 3,
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
    "intervalId": 4,
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
    "intervalId": 5,
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
    "intervalId": 6,
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
    "intervalId": 7,
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
    "intervalId": 8,
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
    "intervalId": 9,
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
  }];

  return function(coordinates) {
    return weatherData;
  }
});
