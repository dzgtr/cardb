from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.POST == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'create_user.html', context)