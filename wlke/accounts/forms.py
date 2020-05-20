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
            if not benutzer:
                raise forms.ValidationError('Dieser Benutzer existiert nicht!')
            if not benutzer.check_password(passwort):
                raise forms.ValidationError('Falsches Passwort!')
            if not benutzer.is_active:
                raise forms.ValidationError('Dieser Benutzer ist nicht aktiv!')
        return super(UserLoginForm, self).clean(*args, **kwargs)
        

                