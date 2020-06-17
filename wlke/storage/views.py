from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Datei

# Create your views here.


def index(response):

    if response.method == "POST":
        neue_datei = response.POST.get('datei')
        # print(neue_datei)
        t = Datei(datei=neue_datei, name=str(
            neue_datei),)
        t.save()
        return HttpResponseRedirect("/storage")

    dateien = Datei.objects.all().order_by("name")
    frontend_data = {'dateien': dateien, }
    return render(response, 'storage/storage_index.html', frontend_data)
