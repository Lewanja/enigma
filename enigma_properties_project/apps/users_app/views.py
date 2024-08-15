from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# from .forms import UserCreationForm

# Create your views here.
from enigma_properties_project.apps.users_app.forms import CustomUserCreationForm


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            obj = User.objects.get(username=username)
            return render(request, "index.html", context={"obj": obj})
        else:
            return HttpResponse("Invalid! User does not exist")

    elif request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'get_login_details.html', context={'form': form})

    else:
        return "Invalid Request"



def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('index')  # Redirect to a home page or some other page
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

