from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=100, null=False)
    cover = models.DecimalField()


STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
)

SOURCE_CHOICES = (
    ('online', 'Online'),
    ('phone', 'Phone'),
    ('in_person', 'In Person'),
)


class Reservation(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    number_of_people = models.IntegerField(default=1)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    custom_user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    special_requests = models.CharField(max_length=255, blank=True)
    staff = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True)
    deposit_paid = models.BooleanField(default=False)
    source = models.CharField(
        max_length=10,
        choices=SOURCE_CHOICES,
        default='online'
    )
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reservation {self.id} for {self.event} on {self.date}"

    class Meta:
        ordering = ['-date', '-start_time']
