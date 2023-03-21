from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class EngineType(models.Model):
    pass

class TransmissionType(models.Model):
    pass

class Car(models.Model):
    #car basic info
    brand = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    additional_model_info = models.CharField(max_length=100)

    #engine info
    displacement = models.DecimalField(max_digits=10, decimal_places=2)
    # engine type
    power = models.IntegerField()
    #dimensions etc


    #suspension info

    added_by = models.CharField(max_length=150)
    points = models.IntegerField(default=0)

class Label():
    def __init__(self, name, tooltip, required=False):
        self.name = name
        self.tooltip = tooltip
        self.required = required


labels = {
    "Description":{
                "brand": Label("Car brand", "(Subaru)", True),
                "model": Label("Model", "(Impreza)", True),
                "additional_model_info": Label("Additional names", "(WRX STI)")},
    "Engine": {
              "displacement": Label("Engine Displacement", "in cm3", True),
              "power": Label("Engine Power", "in HP", True)},
    "Dimensions": {
                "length": Label("Length", "in mm"),
                "width": Label("Width", "in mm"),
                "height": Label("Height", "in mm"),
                "wheelbase": Label("Wheelbase", "in mm")
    }}
