from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.


def login(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        benutzername = form.cleaned_data.get('benutzername')
        passwort = form.cleaned_data.get('passwort')
        benutzer = authenticate(username=benutzername, password=passwort)
        login(request, benutzer)
        if next:
            return redirect(next)
        return redirect('/')
    
    data = {
        'form': form,

    }
    return render(request, 'login.html', data)