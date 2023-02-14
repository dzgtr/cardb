from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)