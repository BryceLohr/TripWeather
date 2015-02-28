from django.conf.urls import patterns, include, url
from django.contrib import admin

from api.views import (
    FlightPlans,
    WeatherForRoute
)


urlpatterns = patterns('',
    url(r'^$', 'ui.views.index'),

    url(r'^api/flight_plan$', FlightPlans.as_view()),
    url(r'^api/weather_for_route/(\d+)$', WeatherForRoute.as_view(), name='weather'),

    url(r'^admin/', include(admin.site.urls)),
)
