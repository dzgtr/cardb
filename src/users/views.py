from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
import secrets

# Create your views here.
def create_user_view(request):
    form = UserCreationForm()
    pform = ProfileForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid() and pform.is_valid():
            form.save()
            pform.save()
            return redirect("create-user-view")

    context = {"form": form, "pform": pform}
    return render(request, "create_user.html", context)

def generate_password():
    return secrets.token_urlsafe(20)
