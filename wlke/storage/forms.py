from django import forms
from .models import Datei


class DateiForm(forms.ModelForm):
    class Meta:
        model = Datei
        fields = ('datei', 'name',)
