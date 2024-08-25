from django.db import models
from accounts.models import Accounts

# Create your models here.


def salon_image_upload_path(instance, filename):
    return f"salon/{instance.salon.id}/{filename}"


STATUS_CHOICES = [
    ("pending", "Pending"),
    ("approved", "Approved"),
    ("rejected", "Rejected"),
]


class Salons(models.Model):
    owner = models.ForeignKey(
        Accounts, related_name="salon_owner", on_delete=models.CASCADE
    )
    salon_name = models.CharField(max_length=50)
    description = models.TextField()
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    services = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def set_services(self, services_list):
        self.services = ",".join(services_list)

    def get_services(self):
        return self.services.split(",")

    def __str__(self):
        return self.salon_name

    class Meta:
        ordering = ("-id",)
        verbose_name_plural = "SALONS"


class SalonImages(models.Model):
    salon = models.ForeignKey(
        Salons, related_name="salon_images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=salon_image_upload_path)

    class Meta:
        verbose_name_plural = "SALONS IMAGES"


class Services(models.Model):
    salon = models.ForeignKey(
        Salons, related_name="salon_service", on_delete=models.CASCADE
    )
    service_name = models.CharField(max_length=50)
    duration = models.IntegerField(default=30)
    price = models.IntegerField(default=500)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.salon.salon_name} -> {self.service_name}"

    class Meta:
        verbose_name_plural = "SALON SERVICES"
