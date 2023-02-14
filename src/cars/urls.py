from django.contrib import admin
from django.urls import path

app_name = 'cars'
from cars.views import all_cars_view

urlpatterns = [
    path('', all_cars_view, name='all-cars-view'),
]
