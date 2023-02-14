from django.shortcuts import render

# Create your views here.
def all_cars_view(request):
    context = {}
    return render(request, "all_cars.html", context)
