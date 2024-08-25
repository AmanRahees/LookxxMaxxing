from django.urls import path
from core.views import *

urlpatterns = [
    path("login", loginView, name="admin-login"),
    path("", dashboard, name="admin-dashboard"),
    path("customers", customers, name="admin-customers"),
    path("outlets", outlets, name="admin-outlets"),
    path("business", businesses, name="admin-businesses"),
    path("reviews", reviews, name="admin-reviews"),
]
