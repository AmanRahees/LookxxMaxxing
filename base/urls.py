from django.urls import path
from base.views import *
from accounts.views import *

urlpatterns = [
    # auth
    path("login", loginView, name="user-login"),
    path("register", registerView, name="user-register"),
    path("logout", logoutView, name="logout"),
    #
    path("", index, name="index"),
    path("salon/<str:name>/<str:encoded_id>", salon_detail, name="salon-detail"),
]
