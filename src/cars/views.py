from django.shortcuts import render
from cars.models import Car

# Create your views here.
def all_cars_view(request):
    context = {}
    return render(request, "all_cars.html", context)

def create_car_view(request):
    fields = []
    for field in Car._meta.get_fields():
        fields.append(field.name)
    context = {"fields":fields, }
    return render(request, "create_car.html", context)