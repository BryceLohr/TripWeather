var TripWeather = function() {

    var FlightPlan = function() {
        var self = this;

        self.departLocation = ko.observable();
        self.arriveLocation = ko.observable();
        self.departTime = ko.observable();
        self.plannedSpeed = ko.observable();
        self.reportInterval = ko.observable();

        self.weatherReports = ko.observableArray();
        self.weatherReportCoordinates = [];

        self.isLoading = ko.observable(false);
        self.errors = ko.observable({});

        self.buildFlightPlan = function() {
            self.isLoading(true);

            self._createFlightPlan()
                .then(self._getWeatherReport)
                .done(self._updateState)
                .always(function() {
                    self.isLoading(false);
                });
        };

        self.hasError = function(fieldName) {
            return !!self.errors()[fieldName];
        };

        self.getErrors = function(fieldName) {
            var errs = self.errors();
            if (errs[fieldName] && errs[fieldName].length > 0) {
                var messages = $.map(errs[fieldName], function(item) { return item.message; });
                return messages.join("<br>");
            }
        }

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
                if (jqxhr.status == 400) {
                    var errorData = JSON.parse(jqxhr.responseText);
                    self.errors(errorData);
                } else {
                    console.error("Request to create flight plan failed: %o\n%o", status, error);
                }
            });
        };

        self._getWeatherReport = function(data, status, jqxhr) {
            var location = jqxhr.getResponseHeader('Location');

            // Return the promise created by ajax() so more actions can be chained
            return $.ajax({
                url: location,
                type: "GET"
            }).fail(function(jqxhr, status, error) {
                console.error("Request to get flight weather failed: %o\n%o", status, error);
            });
        };

        self._updateState = function(data) {
            // Update coords first, since the map update triggered by updating
            // the reports array depends on them being available
            self.weatherReportCoordinates = self._getReportCoordinates(data);
            self.weatherReports(data);
        };

        self._getReportCoordinates = function(data) {
            return $.map(data, function(report) {
                return new google.maps.LatLng(report.latitude, report.longitude);
            });
        };
    };

    ko.bindingHandlers.googleMap = {
        init: function(element, valueAccessor, allBindings, deprecated, bindingContext) {
            var midpoint = new google.maps.LatLng(41.89490005922622, -95.85483831531833);

            var mapOptions = {
                center: midpoint,
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

            bindingContext.$data.map = new google.maps.Map(element, mapOptions);
        },
        update: function(element, valueAccessor, allBindings, deprecated, bindingContext) {
            var weatherData = ko.unwrap(valueAccessor());
            if (weatherData.length < 1) {
                return;
            }

            var coords = bindingContext.$data.weatherReportCoordinates;

            var addWeatherReportToMap = function(map, reportNum, coord) {
                var marker = new google.maps.Marker({
                    position: coord,
                    map: map
                });
                if (weatherData[reportNum].available) {
                    var weatherReport = new google.maps.InfoWindow({
                        position: coord,
                        content: "Weather report for hour "+reportNum+".<br>" +
                          "PrecipProb: "+weatherData[reportNum]["precipProb"]+", temp: "+weatherData[reportNum]["temp"]
                    });
                    google.maps.event.addListener(marker, 'click', function() {
                        weatherReport.open(map, marker);
                    });
                }
            };

            for (var i=0; i<coords.length; i++) {
                addWeatherReportToMap(bindingContext.$data.map, i, coords[i]);
            }

            var flightPath = new google.maps.Polyline({
                path: coords,
                geodesic: true,
                strokeColor: '#FF0000',
                strokeOpacity: 1.0,
                strokeWeight: 2
            });

            flightPath.setMap(bindingContext.$data.map);
        }
    };

    ko.applyBindings(new FlightPlan());

}();
