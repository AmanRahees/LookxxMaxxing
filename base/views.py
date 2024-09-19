from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.timezone import make_aware
from datetime import datetime, timedelta, date
from dateutil import parser
from django.utils.dateparse import parse_datetime
from app.utils import decode_id
from core.mail import sendBookingMail
from business.models import Salons, Services
from core.models import Bookings, Reviews

# Create your views here.


def index(request):
    salons = Salons.objects.all()
    context = {
        "popular": salons,
        "latest": salons,
    }
    return render(request, "pages/frontend/index.html", context)


def salon_detail(request, name, salon_id):
    id = decode_id(salon_id)
    salon = Salons.objects.get(id=id)
    context = {"salon": salon}
    return render(request, "pages/frontend/detail.html", context)


def search_results(request):
    if "search" in request.GET:
        key = request.GET.get("search")
        if key:
            salons = Salons.objects.filter(city__icontains=key)
        else:
            return redirect("index")
    else:
        salons = Salons.objects.all().order_by("-id")
    total_results = salons.count()
    context = {"salons": salons, "total_results": total_results}
    return render(request, "pages/frontend/results.html", context)


def get_available_slots(salon, service, selected_date):
    working_start = make_aware(datetime.combine(selected_date, salon.opening_time))
    working_end = make_aware(datetime.combine(selected_date, salon.closing_time))

    bookings = Bookings.objects.filter(
        service__salon=salon, start_time__date=selected_date
    )

    available_slots = []
    current_time = working_start

    while current_time + timedelta(minutes=service.duration) <= working_end:
        overlap = False
        for booking in bookings:
            booking_start = booking.start_time
            booking_end = booking.end_time
            if not (
                current_time + timedelta(minutes=service.duration) <= booking_start
                or current_time >= booking_end
            ):
                overlap = True
                break

        if not overlap:
            available_slots.append(current_time)

        current_time += timedelta(minutes=service.duration)
    return available_slots


def booking_page(request, name, salon_id, service_id):
    salonId = decode_id(salon_id)
    serviceId = decode_id(service_id)
    salon = Salons.objects.get(id=salonId)
    service = Services.objects.get(id=serviceId)
    selected_date_str = request.GET.get("date")
    if selected_date_str:
        try:
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d").date()
        except:
            selected_date = date.today()
    else:
        selected_date = date.today()
    slots = get_available_slots(salon, service, selected_date)
    context = {
        "slots": slots,
        "service": service,
        "salon": salon,
        "selected_date": selected_date,
    }
    return render(request, "pages/frontend/booking.html", context)


def confirm_booking(request, service_id):
    serviceId = decode_id(service_id)
    service = get_object_or_404(Services, id=serviceId)
    salon = service.salon.salon_name
    if request.method == "POST":
        slot = request.POST.get("slot")
        slot_time = parser.parse(slot)
        print(type(slot_time))
        Bookings.objects.create(
            customer=request.user, service=service, start_time=slot_time
        )
        sendBookingMail(
            request,
            email=request.user.email,
            name=request.user.username,
            salon=salon,
            service=service.service_name,
            time=slot,
        )
        return redirect("index")
    return redirect("index")


def review(request, name, salon_id):
    salon = get_object_or_404(Salons, id=decode_id(salon_id))
    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        Reviews.objects.create(
            customer=request.user, salon=salon, rating=rating, comment=comment
        )
        return redirect(reverse("salon-detail", args=[name, salon_id]))
