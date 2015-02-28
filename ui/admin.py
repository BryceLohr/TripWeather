from django.contrib import admin
from ui.models import Airport


class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'iata_faa', 'city', 'country')


admin.site.register(Airport, AirportAdmin)
