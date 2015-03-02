import json

from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseNotFound
from restless.views import Endpoint
from restless.models import serialize

from api import flight_plan


class FlightPlans(Endpoint):
    def post(self, request):
        try:
            form = flight_plan.FlightPlanForm(request.data)
            if form.is_valid():
                (plan, weather) = flight_plan.build_flight_plan(form)
                flight_plan_id = flight_plan.persist(plan, weather)

                response = HttpResponse(status=201)
                # This should really go to a resource describing the flight plan itself, but this is fine for now
                response['Location'] = reverse('weather', args=[flight_plan_id])
                return response
            else:
                return HttpResponse(form.errors.as_json(), status=400, content_type="text/json")
        except ValueError:
            return HttpResponse("Invalid JSON document", status=415)


class WeatherForRoute(Endpoint):
    def get(self, request, flight_plan_id):
        try:
            plan = flight_plan.get_flight_plan(flight_plan_id)
            return serialize(plan, include=[('weatherreport_set', dict())])
        except flight_plan.NotFound:
            return HttpResponseNotFound()
