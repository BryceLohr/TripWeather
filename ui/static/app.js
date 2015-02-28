angular.module('TripWeather', ['uiGmapgoogle-maps', 'FlightPlan', 'WeatherData'])

.config(function(uiGmapGoogleMapApiProvider) {
    uiGmapGoogleMapApiProvider.configure({
        key: GOOGLE_API_KEY,
        v: '3.17'
    });
})

.controller('MapController', ['$scope', 'getWeatherReportCoords', 'getWeatherAtCoords',
    function($scope, getWeatherReportCoords, getWeatherAtCoords) {
  var departureLocation = { latitude: 40.639751, longitude: -73.778925 }; // JFK
  var arrivalLocation = { latitude: 37.618972, longitude: -122.374889 }; // SFO
  var departTime = new Date(2015, 1, 7, 8);
  var avgSpeed = 300; // miles per hour
  var reportInterval = 1; // hours

  $scope.weatherReportCoordinates = getWeatherReportCoords(
    departureLocation, arrivalLocation, departTime, avgSpeed, reportInterval);

  $scope.weatherReports = getWeatherAtCoords($scope.weatherReportCoordinates);

  console.log("weatherReportCoordinates: ", $scope.weatherReportCoordinates);
  console.log("weatherReports: ", $scope.weatherReports);

  $scope.mapOptions = {
    center: $scope.weatherReportCoordinates.midpoint,
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
}]);
