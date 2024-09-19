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
    path("salons", search_results, name="results"),
    path("salon/<str:name>/<str:salon_id>", salon_detail, name="salon-detail"),
    path(
        "booking/<str:name>/<str:salon_id>/<str:service_id>",
        booking_page,
        name="service-details",
    ),
    path(
        "confirm/<str:service_id>",
        confirm_booking,
        name="confirm-booking",
    ),
    path(
        "review/<str:name>/<str:salon_id>",
        review,
        name="review-salon",
    ),
]
