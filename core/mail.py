from django.conf import settings
from django.core.mail import send_mail
import random


def sendBookingMail(request, email, name, salon, service, time):
    subject = "Booking"
    message = (
        f"Hello {name}!\n\n"
        f"Thank you for choosing Lookxxmaxxing for your {service} booking!\n\n"
        f"We are excited to confirm your booking at our salon, {salon}. Your booking is scheduled for {time}. "
        f"See you soon at Lookxxmaxxing!\n\n"
        f"Best regards,\n"
        f"The Lookxxmaxxing"
    )
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [
        email,
    ]
    send_mail(subject, message, email_from, recipient_list)
