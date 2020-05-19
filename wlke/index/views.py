from django.shortcuts import render

from .models import Jumbo

# Create your views here.


def index(request):
    jumbo_data = Jumbo.objects.get(pk=1)
    frontend_data = {'jumbo_data': jumbo_data, }
    return render(request, 'index/index.html', frontend_data)
