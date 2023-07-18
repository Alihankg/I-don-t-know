from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        messages.warning(request, "You should logout first before you register again!")
        return redirect("/")
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/')
        else:
            form = RegisterForm()
        return render(request, "register/register.html", {"form":form})
    
def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in!")
        return redirect("/")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                auth.login(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password!")
                return redirect("/login")
        else:
            form = AuthenticationForm()
            return render(request, "registration/login.html", {"form": form})
        
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "Succesfully logged out!")
        return redirect("/")
    else:
        messages.warning(request, "Haven't logged in yet!")
        return redirect("/")