from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User

import secrets
import json

# Create your views here.
def create_user_view(request):
    form = UserCreationForm(request.POST)
    pform = ProfileForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = request.POST.copy()
            if post['birth_date'] == "":
                post['birth_date'] = "1900-01-01"
            request.POST = post
            form.save()
            pform.save()
            messages.success(request, 'Your profile is created')
            return redirect("create-user-view")

    context = {"form": form, "pform": pform}
    return render(request, "create_user.html", context)

def generate_password():
    return secrets.token_urlsafe(20)
