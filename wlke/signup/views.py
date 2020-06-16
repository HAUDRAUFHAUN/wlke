from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from .forms import SignupForm

import os
from django.views.decorators.csrf import csrf_protect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.

@csrf_protect
def signup(response):
    if response.method == "POST":
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()

            # Get nutzername to create user specific folder
            nutzername = response.POST.get('username')
            # print(nutzername)

            benutzerdir = os.path.join(
                BASE_DIR, './media/data/{{ nutzername }}/')
            os.mkdir(path=benutzerdir)

            return redirect('/storage')
    else:
        form = SignupForm
    return render(response, 'signup/signup.html', {'form': form})


def logout(request):
    return render(request, 'registration/logout.html')
