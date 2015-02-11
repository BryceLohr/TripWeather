from django.conf.urls import patterns, include, url
from django.contrib import admin

from api.views import (
    FlightPlan,
    WeatherForRoute,
    WeatherForRouteDetail
)


urlpatterns = patterns('',
    url(r'^$', 'api.views.index'),

    url(r'^flight_plan$', FlightPlan.as_view()),
    url(r'^weather_for_route$', WeatherForRoute.as_view()),
    url(r'^weather_for_route/(\d+)$', WeatherForRouteDetail.as_view(), name='weather_detail'),

    url(r'^admin/', include(admin.site.urls)),
)
