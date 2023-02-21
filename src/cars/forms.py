from django import forms
from models import Car, labels


class CarCreateForm(forms.ModelForm):
    form = {}
    for field in Car._meta.get_fields():
        form[field.name] = forms.CharField()
