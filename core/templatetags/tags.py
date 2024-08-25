from django import template
from django.urls import reverse
from app.utils import encode_id, decode_id
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
