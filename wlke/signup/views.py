from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from .forms import SignupForm

# Create your views here.


def signup(response):
    if response.method == "POST":
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect('/storage')
    else:
        form = SignupForm
    return render(response, 'signup/signup.html', {'form': form})
