from django.contrib.auth.models import User
from django.forms import ModelForm
from users.models import Profile
from django.db.models import DateField
from django.conf.global_settings import DATE_INPUT_FORMATS

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'birth_date')

