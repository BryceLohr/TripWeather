from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {'google_api_key': settings.GOOGLE_API_KEY}
    return render(request, 'index.html', context)


