from django.conf.urls import patterns, include, url
from django.contrib import admin

from api.views import FlightPlan


urlpatterns = patterns('',
    url(r'^$', 'api.views.index'),

    url(r'^flight_plan$', FlightPlan.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
