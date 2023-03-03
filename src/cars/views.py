from django.shortcuts import render
from cars.models import Car, labels
from cars.forms import CarCreateForm

# Create your views here.
def all_cars_view(request):
    context = {}
    return render(request, "all_cars.html", context)

def create_car_view(request):
    if request.method == "POST":
        pass
    form = CarCreateForm(request.POST)
    labelsdict = {}
    for key, value in labels.items():
        labelsdict[key] = [labels[key].name, labels[key].tooltip, labels[key].required]

    context = {"form": form, "labels": labelsdict}
    return render(request, "create_car.html", context)