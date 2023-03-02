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

    context = {"form": form, "labels": labels}
    return render(request, "create_car.html", context)