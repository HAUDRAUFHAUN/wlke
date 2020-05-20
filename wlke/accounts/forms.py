from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

Benutzer = get_user_model()


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


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='E-Mail Adresse')
    email2 = forms.EmailField(label='E-Mail Bestätigung')
    passwort = forms.CharField(widget=forms.PasswordInput)
    passwort2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Benutzer
        fields = [
            'benutzername',
            'email',
            'email2',
            'passwort',
            'passwort2',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        passwort = self.cleaned_data.get('passwort')
        passwort2 = self.cleaned_data.get('passwort2')

        if email != email2:
            raise forms.ValidationError('E-Mail Adressen stimmen nicht überein!')

        email_qs = Benutzer.objects.filter(email=email)

        if email_qs.exists():
            raise forms.ValidationError('DieseE-Mail wurde bereits registriert!')

        return email

        if passwort != passwort2:
            raise forms.ValidationError('Passwörter müssen übereinstimmen!')


        