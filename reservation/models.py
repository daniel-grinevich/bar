from django.core.exceptions import ValidationError
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
    event = models.ForeignKey("Event", on_delete=models.CASCADE, null=True, blank=True)
    number_of_people = models.IntegerField(default=1)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date = models.DateField()
    custom_user = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    location = models.ForeignKey("location.Location", on_delete=models.CASCADE)
    table = models.ForeignKey("location.Table", on_delete=models.CASCADE)
    special_requests = models.CharField(max_length=255, blank=True)
    deposit_paid = models.BooleanField(default=False)
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default="online")
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reservation {self.id} for {self.event} on {self.date}"

    def save(self, *args, **kwargs):

        if not self.end_time and self.start_time:
            self.end_time = self.start_time + timedelta(hours=2)

        conflicting_reservations_query = Reservation.objects.filter(
            table=self.table,
            location=self.location,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        )

        if self.pk:
            conflicting_reservations_query = conflicting_reservations_query.exclude(
                pk=self.pk
            )

        # Check if any conflicting reservations exist
        if conflicting_reservations_query.exists():
            raise ValidationError("A conflicting reservation exists.")

        if not self.date:
            self.date = self.start_time.date()

        super().save(*args, **kwargs)

    @classmethod
    def get_week_of_reservations(cls, reference_date=None, location=None):
        """
        Fetches reservations from a day before the reference_date to five day
        after given a location.

        :param reference_date: The date around which to fetch reservations.
        :type reference_date: datetime.date or None
        :param location: The Locaation to query reservations from
        :type: String or None
        :return: QuerySet of Reservation objects within the specified date range.
        :rtype: django.db.models.QuerySet
        """
        if reference_date is None:
            reference_date = timezone.localdate()  # Ensure timezone-aware comparison
        start_date = reference_date - timedelta(days=1)
        end_date = reference_date + timedelta(days=5)

        if location:
            return cls.objects.filter(
                date__range=(start_date, end_date), location__name=location
            )

        return cls.objects.filter(date__range=(start_date, end_date))

    @classmethod
    def get_reservation_list(cls, reference_date, location, status, time):
        """
        Get reservations based on location & date should have both passed in.
        """
        if reference_date and location and status:
            return cls.objects.filter(
                location__name=location,
                date=reference_date,
                status=status,
                start_time__gt=time,
            )

    def reservation_detail(self):
        return f"Location: {self.location.name} Table: {self.table.name} Ppl: {self.number_of_people}"

    class Meta:
        ordering = ["-date", "-start_time"]
