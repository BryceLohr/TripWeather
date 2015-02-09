angular.module('TripWeather', ['uiGmapgoogle-maps'])

.config(function(uiGmapGoogleMapApiProvider) {
    uiGmapGoogleMapApiProvider.configure({
        key: GOOGLE_API_KEY,
        v: '3.17'
    });
})

.controller('MapController', ['$scope', function($scope) {
  $scope.departureLocation = new google.maps.LatLng(40.639751,-73.778925); // JFK
  $scope.arrivalLocation = new google.maps.LatLng(37.618972,-122.374889); // SFO
  $scope.departTime = new Date(2015, 1, 7, 8);
  $scope.avgSpeed = 300; // miles per hour
  $scope.reportInterval = 1; // hours

  $scope.weatherReportCoordinates = [
    $scope.departureLocation,
    // new google.maps.LatLng(40.639751000000004,-73.778925),
    new google.maps.LatLng(41.34843913707863,-79.19563578614297),
    new google.maps.LatLng(41.79828792276403,-84.7094528354295),
    new google.maps.LatLng(41.98152391306366,-90.27792457775081),
    new google.maps.LatLng(41.89490005922622,-95.85483831531833),
    new google.maps.LatLng(41.53995731818525,-101.39338776897682),
    new google.maps.LatLng(40.922899672836124,-106.84943687506541),
    new google.maps.LatLng(40.05410602614879,-112.18435700307927),
    new google.maps.LatLng(38.9473669863364,-117.36703748446496),
    $scope.arrivalLocation
  ]

  $scope.mapOptions = {
    // angular-google-maps doesn't support google.map.LatLng objects
    center: {
      latitude: $scope.weatherReportCoordinates[5].lat(),
      longitude: $scope.weatherReportCoordinates[5].lng()
    },
    mapTypeId: google.maps.MapTypeId.TERRAIN,
    zoom: 5
  };
  $scope.lineOptions = {
    stroke: {
      color: '#FF0000',
      weight: 2,
      opacity: 1.0
    },
    geodesic: true
  }
  // var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  /*
  var addWeatherReportToMap = function(map, reportNum, coords) {
    var marker = new google.maps.Marker({
        position: coords,
        map: map
    });
    var weatherReport = new google.maps.InfoWindow({
      position: coords,
      content: "Weather report for hour "+reportNum+".<br>" +
        "PrecipProb: "+weatherData[reportNum]["precipProb"]+", temp: "+weatherData[reportNum]["temp"]
    });
    google.maps.event.addListener(marker, 'click', function() {
      weatherReport.open(map, marker);
    });
  };

  for (var i=0; i<weatherReportCoordinates.length; i++) {
    addWeatherReportToMap(map, i, weatherReportCoordinates[i]);
  }

  var flightPath = new google.maps.Polyline({
    path: weatherReportCoordinates,
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  flightPath.setMap(map);
  */

    var weatherData = [
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
     }];
}]);
