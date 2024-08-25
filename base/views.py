from django.shortcuts import render
from app.utils import decode_id
from business.models import Salons

# Create your views here.


def index(request):
    salons = Salons.objects.all()
    context = {
        "popular": salons,
        "latest": salons,
    }
    return render(request, "pages/frontend/index.html", context)


def salon_detail(request, name, encoded_id):
    id = decode_id(encoded_id)
    salon = Salons.objects.get(id=id)
    context = {"salon": salon}
    return render(request, "pages/frontend/detail.html", context)
