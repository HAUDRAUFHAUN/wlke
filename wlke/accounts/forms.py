from django import forms
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):
    benutzername = forms.CharField()
    passwort = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        benutzername = self.cleaned_data.get('benutzername')
        passwort = self.cleaned_data('passwort')

        if benutzername and passwort:
            benutzer = authenticate(username=benutzername, password=passwort)
            if not user:
                raise forms.ValidationError('Dieser Benutzer existiert nicht')