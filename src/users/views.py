from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def create_user_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create-user-view")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "create_user.html", context)

def generate_password():
    return secrets.token_urlsafe(20)
