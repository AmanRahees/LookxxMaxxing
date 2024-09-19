from django import template
from django.urls import reverse
from datetime import datetime, timedelta
from app.utils import encode_id, decode_id
from core.models import Bookings
import re

register = template.Library()


@register.simple_tag
def sidebar_items():
    items = [
        {
            "name": "Dashboard",
            "url_name": "admin-dashboard",
            "url_for": reverse("admin-dashboard"),
            "icon": "fa-solid fa-gauge-high",
        },
        {
            "name": "Customers",
            "url_name": "admin-customers",
            "url_for": reverse("admin-customers"),
            "icon": "fa-solid fa-users",
        },
        {
            "name": "Outlets",
            "url_name": "admin-outlets",
            "url_for": reverse("admin-outlets"),
            "icon": "fa-solid fa-shop",
        },
        {
            "name": "Business",
            "url_name": "admin-businesses",
            "url_for": reverse("admin-businesses"),
            "icon": "fa-solid fa-briefcase",
        },
        {
            "name": "Reviews",
            "url_name": "admin-reviews",
            "url_for": reverse("admin-reviews"),
            "icon": "fa-solid fa-comment-dots",
        },
    ]
    return items


@register.filter
def format_url(name):
    if not name:
        return ""
    formatted_name = re.sub(r"\s+", "-", name).lower()
    return formatted_name


@register.filter
def encode(value):
    return encode_id(value)


@register.filter
def set_range(value):
    return range(value)


@register.simple_tag
def tomorrow_date():
    return (datetime.now() + timedelta(days=1)).date()


@register.simple_tag
def has_booked_service(user, salon_id):
    if not user.is_authenticated:
        return False
    return Bookings.objects.filter(customer=user, service__salon_id=salon_id).exists()


@register.filter(name="rating_of")
def rating_of(value, arg):
    return range(value, arg + 1)


@register.filter(name="average_rating")
def average_rating(reviews):
    if reviews.exists():
        total_reviews = reviews.count()
        total_rating = sum([review.rating for review in reviews])
        return round(total_rating / total_reviews, 1)
    return 0.0
