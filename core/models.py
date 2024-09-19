from django.db import models
from datetime import timedelta
from business.models import Accounts, Services, Salons

# Create your models here.


class Bookings(models.Model):
    customer = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, related_name="booked_by"
    )
    service = models.ForeignKey(
        Services, on_delete=models.CASCADE, related_name="booked_service"
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.end_time = self.start_time + timedelta(minutes=int(self.service.duration))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "BOOKINGS"


class Reviews(models.Model):
    customer = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, related_name="review_by"
    )
    salon = models.ForeignKey(
        Salons, on_delete=models.CASCADE, related_name="salon_review"
    )
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer.username} for {self.salon.salon_name} - Rating: {self.rating}"

    class Meta:
        verbose_name_plural = "REVIEWS"
