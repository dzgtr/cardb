from django.db.models import IntegerField
from django.contrib.auth.models import User

class CustomUser(User):
    points = IntegerField()
