from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.storage import FileSystemStorage


from .models import Datei
from .forms import DateiForm


def index(request):
    if request.method == 'POST':
        form = DateiForm(request.POST, request.FILES, request.user)
        if form.is_valid():
            formfile = Datei(benutzer=request.user,
                             datei=form.datei, name=form.name)
            return redirect('/storage/')
    else:
        form = DateiForm()

    return render(request, 'storage/storage_index.html', {
        'form': form,
    })
