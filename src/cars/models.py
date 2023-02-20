from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class EngineType(models.Model):
    pass

class Car(models.Model):
    #car basic info
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    additional_model_info = models.CharField(max_length=100)

    #engine info
    displacement = models.DecimalField(max_digits=10, decimal_places=2, validators=MinValueValidator(1))
    # engine type
    power = models.IntegerField(validators=MinValueValidator(0))
    #dimensions etc


    #suspension info
