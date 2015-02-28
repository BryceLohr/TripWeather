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
            this.weatherReports(weatherData);
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
        "cldCvr": 1,
        "temp": 23.8,
        "flight_plan": 3,
        "timestamp": "2015-02-28T01:30:09Z",
        "sfcPres": 1033.7,
        "longitude": -73.778925,
        "windDir": 323.2,
        "precip": 0,
        "spcHum": 1.1,
        "snowfall": 0,
        "windSpd": 9.1,
        "snowfallProb": null,
        "latitude": 40.639751,
        "id": 12,
        "precipProb": 0
    },
    {
        "cldCvr": 16,
        "temp": -0.9,
        "flight_plan": 3,
        "timestamp": "2015-02-28T02:30:09Z",
        "sfcPres": 1040.3,
        "longitude": -79.4507028903156,
        "windDir": 280.1,
        "precip": 0,
        "spcHum": 0.8,
        "snowfall": 0,
        "windSpd": 0,
        "snowfallProb": null,
        "latitude": 41.3752253488061,
        "id": 13,
        "precipProb": 0
    },
    {
        "cldCvr": 30,
        "temp": 5,
        "flight_plan": 3,
        "timestamp": "2015-02-28T03:30:09Z",
        "sfcPres": 1040.8,
        "longitude": -85.2267612152091,
        "windDir": 240,
        "precip": 0,
        "spcHum": 0.8,
        "snowfall": 0,
        "windSpd": 3,
        "snowfallProb": null,
        "latitude": 41.8267133364137,
        "id": 14,
        "precipProb": 0
    },
    {
        "cldCvr": 1,
        "temp": -6.1,
        "flight_plan": 3,
        "timestamp": "2015-02-28T04:30:09Z",
        "sfcPres": 1041.7,
        "longitude": -91.0580620400133,
        "windDir": 204.6,
        "precip": 0,
        "spcHum": 0.6,
        "snowfall": 0,
        "windSpd": 3,
        "snowfallProb": null,
        "latitude": 41.9856558083083,
        "id": 15,
        "precipProb": 0
    },
    {
        "cldCvr": 17.4,
        "temp": 7,
        "flight_plan": 3,
        "timestamp": "2015-02-28T05:30:09Z",
        "sfcPres": 1036.9,
        "longitude": -96.8913978529929,
        "windDir": 150,
        "precip": 0,
        "spcHum": 0.9,
        "snowfall": 0,
        "windSpd": 7,
        "snowfallProb": null,
        "latitude": 41.8489656306218,
        "id": 16,
        "precipProb": 0
    },
    {
        "cldCvr": 73.6,
        "temp": 11.1,
        "flight_plan": 3,
        "timestamp": "2015-02-28T06:30:09Z",
        "sfcPres": 1025.9,
        "longitude": -102.673404662911,
        "windDir": 170,
        "precip": 0,
        "spcHum": 1.3,
        "snowfall": 0,
        "windSpd": 15.8,
        "snowfallProb": null,
        "latitude": 41.4193000878005,
        "id": 17,
        "precipProb": 0
    },
    {
        "cldCvr": 68,
        "temp": 20.9,
        "flight_plan": 3,
        "timestamp": "2015-02-28T07:30:09Z",
        "sfcPres": 1011.8,
        "longitude": -108.354602779854,
        "windDir": 100,
        "precip": 0,
        "spcHum": 2,
        "snowfall": 0,
        "windSpd": 3,
        "snowfallProb": null,
        "latitude": 40.7048260560287,
        "id": 18,
        "precipProb": 0
    },
    {
        "cldCvr": 98.3,
        "temp": 30,
        "flight_plan": 3,
        "timestamp": "2015-02-28T08:30:09Z",
        "sfcPres": 1003.9,
        "longitude": -113.892766300908,
        "windDir": 141.7,
        "precip": 0.01,
        "spcHum": 2.6,
        "snowfall": 0.12,
        "windSpd": 3.9,
        "snowfallProb": null,
        "latitude": 39.718525821211,
        "id": 19,
        "precipProb": 48.44
    },
    {
        "cldCvr": 80.9,
        "temp": 50.6,
        "flight_plan": 3,
        "timestamp": "2015-02-28T10:06:06.537Z",
        "sfcPres": 1007.5,
        "longitude": -122.374889,
        "windDir": 306.3,
        "precip": 0,
        "spcHum": 7.3,
        "snowfall": 0,
        "windSpd": 17.6,
        "snowfallProb": null,
        "latitude": 37.618972,
        "id": 20,
        "precipProb": 30
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
        zoom: 4
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
        if (weatherData[reportNum]) {
            var weatherReport = new google.maps.InfoWindow({
              position: coords,
              content: "Weather report for hour "+reportNum+".<br>" +
                "PrecipProb: "+weatherData[reportNum]["precipProb"]+", temp: "+weatherData[reportNum]["temp"]
            });
            google.maps.event.addListener(marker, 'click', function() {
              weatherReport.open(map, marker);
            });
        }
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

    ko.applyBindings(new FlightPlan());

    return {drawMap: drawMap};

}();
