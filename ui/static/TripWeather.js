var TripWeather = function() {

    var FlightPlan = function() {
        this.depart_location = ko.observable();
        this.arrive_location = ko.observable();
        this.depart_time = ko.observable();
        this.planned_speed = ko.observable();
        this.report_interval = ko.observable();

        this.weatherReports = ko.observableArray();

        this.buildFlightPlan = function() {
            // Show busy indicator
            // Post form to API
            // Get URL for new flight plan's weather
            // Request weather, store in weatherReports
            // Hide busy indicator
        };
    };

    /*
    var WeatherReports = function() {
        this.timestamp = ko.observable();
        this.latitude = ko.observable();
        this.longitude = ko.observable();
        this.cldCvr = ko.observable();
        this.precip = ko.observable();
        this.precipProb = ko.observable();
        this.sfcPres = ko.observable();
        this.snowfall = ko.observable();
        this.snowfallProb = ko.observable();
        this.spcHum = ko.observable();
        this.temp = ko.observable();
        this.windSpd = ko.observable();
        this.windDir = ko.observable();
    }
    */

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

    var drawMap = function() {

      var departureLocation = { latitude: 40.639751, longitude: -73.778925 }; // JFK
      var arrivalLocation = { latitude: 37.618972, longitude: -122.374889 }; // SFO
      var departTime = new Date(2015, 1, 7, 8);
      var avgSpeed = 300; // miles per hour
      var reportInterval = 1; // hours

      var weatherReportCoordinates = [
        new google.maps.LatLng(40.639751, -73.778925),
        new google.maps.LatLng(41.34843913707863, -79.19563578614297),
        new google.maps.LatLng(41.79828792276403, -84.7094528354295),
        new google.maps.LatLng(41.98152391306366, -90.27792457775081),
        new google.maps.LatLng(41.89490005922622, -95.85483831531833),
        new google.maps.LatLng(41.53995731818525, -101.39338776897682),
        new google.maps.LatLng(40.922899672836124, -106.84943687506541),
        new google.maps.LatLng(40.05410602614879, -112.18435700307927),
        new google.maps.LatLng(38.9473669863364, -117.36703748446496),
        new google.maps.LatLng(37.618972, -122.374889)
      ];
      weatherReportCoordinates.midpoint = new google.maps.LatLng(41.89490005922622, -95.85483831531833);

      var mapOptions = {
        center: weatherReportCoordinates.midpoint,
        mapTypeId: google.maps.MapTypeId.TERRAIN,
        zoom: 5
      };

      var lineOptions = {
        stroke: {
          color: '#FF0000',
          weight: 2,
          opacity: 1.0
        },
        geodesic: true
      };

      var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

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
    };

    return {drawMap: drawMap};

}();