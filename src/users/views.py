from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProfileForm
import secrets
import json

# Create your views here.
def create_user_view(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        pform = ProfileForm(request.POST)
        if form.is_valid():
            post = request.POST.copy()
            print(post)
            if post['birth_date'] == "":
                post['birth_date'] = "1900-01-01"
            print(post)
            request.POST = post
            form.save()
            pform.save()
            messages.success(request, 'Your profile is created')
            return redirect("create-user-view")
    else:
        form = UserCreationForm()
        pform = ProfileForm()

    context = {"form": form, "pform": pform}
    return render(request, "create_user.html", context)

def generate_password():
    return secrets.token_urlsafe(20)
