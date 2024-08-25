from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.models import Accounts

# Create your views here.


def loginView(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, "Invalid credentials!")
    return redirect("/")


def registerView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if Accounts.objects.filter(email=email).exists():
            messages.error(request, "You are already Registered. Please log in.")
        else:
            user = Accounts.objects.create_user(
                username=username, email=email, password=password
            )
            login(request, user)
            messages.success(request, "Your account has been created successfully!")
    return redirect("/")


def logoutView(request):
    logout(request)
    return redirect("index")
