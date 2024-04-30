from django.db import models
from django.utils import timezone


# Create your models here.
class Order(models.Model):
    custom_user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    customer = models.CharField(max_length=255, blank=True, null=True)
    items = models.ManyToManyField("recipe.MenuItem", through="OrderItem")
    total = models.FloatField(default=0)
    tip = models.FloatField(default=0)
    date_time = models.DateTimeField(default=timezone.now)
    reservation = models.ForeignKey(
        "reservation.Reservation", on_delete=models.CASCADE, related_name="orders"
    )
    PLACED = "placed"
    PREPARING = "preparing"
    COMPLETED = "completed"
    CANCELED = "canceled"
    STATUS_CHOICES = [
        (PLACED, "Placed"),
        (PREPARING, "Preparing"),
        (COMPLETED, "completed"),
        (CANCELED, "Canceled"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PLACED)

    def __str__(self):
        return f"Order {self.id} - Status: {self.get_status_display()}"

    def save(self, *args, **kwargs):
        if self.custom_user and not self.customer:
            self.customer = self.custom_user.name
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey("recipe.MenuItem", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} for Order {self.order.id}"


class Payment(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    amount = models.FloatField()
    method = models.CharField(
        max_length=10,
        choices=[
            ("credit", "Credit"),
            ("cash", "Cash"),
            ("gift", "Gift"),
            ("free", "Free"),
        ],
        default="credit",
    )
    date_time = models.DateTimeField(default=timezone.now)


class PaymentDetail(models.Model):
    payment = models.OneToOneField(
        Payment, on_delete=models.CASCADE, related_name="details"
    )
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    payer_details = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(
        max_length=100, default="completed", null=True, blank=True
    )
    notes = models.TextField(null=True, blank=True)
