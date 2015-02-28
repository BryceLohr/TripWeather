from django.contrib import admin
from api.models import FlightPlan, WeatherReport


class FlightPlanAdmin(admin.ModelAdmin):
    list_display = ('depart_time', 'id', 'depart_latitude', 'depart_longitude')


class WeatherReportAdmin(admin.ModelAdmin):
    list_display = ('flight_plan', 'id', 'timestamp', 'latitude', 'longitude')


admin.site.register(FlightPlan, FlightPlanAdmin)
admin.site.register(WeatherReport, WeatherReportAdmin)
