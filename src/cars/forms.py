from django import forms
from cars.models import Car, labels


class CarCreateForm(forms.ModelForm):
    form = {}
    for field in Car._meta.get_fields():
        form[field.name] = forms.CharField(widget=forms.TextInput(attrs={'class': 'car_input'}))

    class Meta:
        model = Car
        fields = ["brand"]