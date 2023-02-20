from django.contrib import admin
from django.urls import path

app_name = 'cars'
from cars.views import all_cars_view
from cars.views import create_car_view

urlpatterns = [
    path('', all_cars_view, name='all-cars-view'),
    path('create', create_car_view, name='create-car-view'),
]
