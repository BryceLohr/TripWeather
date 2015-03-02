var TripWeather = function() {

    var FlightPlan = function() {
        var self = this;

        self.departLocation = ko.observable();
        self.arriveLocation = ko.observable();
        self.departTime = ko.observable();
        self.plannedSpeed = ko.observable();
        self.reportInterval = ko.observable();

        self.weatherReports = ko.observableArray();

        self.isLoading = ko.observable(false);

        self.buildFlightPlan = function() {
            self.isLoading(true);

            self._createFlightPlan()
                .then(self._getWeatherReport)
                .done(function(data) {
                    self.weatherReports(data);
                })
                .always(function() {
                    self.isLoading(false);
                });
        };

        self._createFlightPlan = function() {
            var flightParams = {
                depart_location: self.departLocation(),
                arrive_location: self.arriveLocation(),
                depart_time: self.departTime(),
                planned_speed: self.plannedSpeed(),
                report_interval: self.reportInterval()
            };

            // Return the promise created by ajax() so more actions can be chained
            return $.ajax({
                url: "/api/flight_plan",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify(flightParams)
            }).fail(function(jqxhr, status, error) {
                console.error("Request to create flight plan failed:");
                console.log(jqxhr, status, error);
            });
        };

        self._getWeatherReport = function(data, status, jqxhr) {
            var location = jqxhr.getResponseHeader('Location');

            // Return the promise created by ajax() so more actions can be chained
            return $.ajax({
                url: location,
                type: "GET"
            }).fail(function(jqxhr, status, error) {
                console.error("Request to get flight weather failed:");
                console.log(jqxhr, status, error);
            });
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
