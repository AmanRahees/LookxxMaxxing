from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


@never_cache
def loginView(request):
    if request.user.is_authenticated and request.user.is_superadmin:
        return redirect("admin-dashboard")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_superadmin:
                login(request, user)
                return redirect("admin-dashboard")
            else:
                messages.error(request, "Access Denied!")
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, "pages/backend/login.html")


@never_cache
@staff_member_required(login_url="admin-login")
def dashboard(request):
    return render(request, "pages/backend/dashboard.html")


@never_cache
@staff_member_required(login_url="admin-login")
def customers(request):
    return render(request, "pages/backend/customers.html")


@never_cache
@staff_member_required(login_url="admin-login")
def businesses(request):
    return render(request, "pages/backend/businesses.html")


@never_cache
@staff_member_required(login_url="admin-login")
def outlets(request):
    return render(request, "pages/backend/outlets.html")


@never_cache
@staff_member_required(login_url="admin-login")
def reviews(request):
    return render(request, "pages/backend/reviews.html")
