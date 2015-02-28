angular.module('FlightPlan', [])
.factory('getWeatherReportCoords', function() {

  var weatherReportCoordinates = [
    { intervalId: 0, latitude: 40.639751, longitude: -73.778925 },
    { intervalId: 1, latitude: 41.34843913707863, longitude: -79.19563578614297 },
    { intervalId: 2, latitude: 41.79828792276403, longitude: -84.7094528354295 },
    { intervalId: 3, latitude: 41.98152391306366, longitude: -90.27792457775081 },
    { intervalId: 4, latitude: 41.89490005922622, longitude: -95.85483831531833 },
    { intervalId: 5, latitude: 41.53995731818525, longitude: -101.39338776897682 },
    { intervalId: 6, latitude: 40.922899672836124, longitude: -106.84943687506541 },
    { intervalId: 7, latitude: 40.05410602614879, longitude: -112.18435700307927 },
    { intervalId: 8, latitude: 38.9473669863364, longitude: -117.36703748446496 },
    { intervalId: 9, latitude: 37.618972, longitude: -122.374889 },
  ];

  weatherReportCoordinates.midpoint = {
    latitude: 41.89490005922622, longitude: -95.85483831531833
  }

  return function(depart, arrive, departAt, avgSpeed, reportInterval) {
    return weatherReportCoordinates;
  }
})
