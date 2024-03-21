from django.db import models
from django.utils import timezone
from datetime import timedelta


class Event(models.Model):
    name = models.CharField(max_length=100, null=False)
    cover = models.DecimalField(max_digits=6, decimal_places=2)


STATUS_CHOICES = (
    ("pending", "Pending"),
    ("confirmed", "Confirmed"),
    ("cancelled", "Cancelled"),
)

SOURCE_CHOICES = (
    ("online", "Online"),
    ("phone", "Phone"),
    ("in_person", "In Person"),
)


class Reservation(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    number_of_people = models.IntegerField(default=1)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    custom_user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    location = models.ForeignKey("location.Location", on_delete=models.CASCADE)
    special_requests = models.CharField(max_length=255, blank=True)
    # staff = models.ForeignKey("Staff", on_delete=models.SET_NULL, null=True)
    deposit_paid = models.BooleanField(default=False)
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default="online")
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reservation {self.id} for {self.event} on {self.date}"

    def save(self, *args, **kwargs):
        if not self.end_time and self.start_time:
            self.end_time = self.start_time + timedelta(hours=2)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-date", "-start_time"]
