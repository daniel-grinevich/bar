from django.db import models
from django.utils import timezone


class Payment(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
    )
    total = models.FloatField()
    CREDIT = 'credit'
    CASH = 'cash'
    GIFT = 'gift'
    FREE = 'free'
    METHOD_CHOICES = [
        (CREDIT, 'credit'),
        (CASH, 'cash'),
        (GIFT, 'gift'),
        (FREE, 'free'),
    ]
    method = models.CharField(
        max_length=10,
        choices=METHOD_CHOICES,
        default=CREDIT
    )
    date_time = models.DateTimeField(default=timezone.now)


# Create your models here.
class Order(models.Model):
    custom_user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    customer = models.CharField(max_length=255, blank=True, null=True)
    itmes = models.ManyToManyField('Item', through='OrderItem')
    # this may need to be taken out
    total = models.FloatField()
    date_time = models.DateTimeField(default=timezone.now)
    # this may need to be taken out
    tip = models.FloatField()
    reservation = models.ForeignKey(
        'reservation.Reservation',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    PLACED = 'placed'
    PREPARING = 'preparing'
    COMPLETED = 'completed'
    CANCELED = 'canceled'
    STATUS_CHOICES = [
        (PLACED, 'Placed'),
        (PREPARING, 'Preparing'),
        (COMPLETED, 'completed'),
        (CANCELED, 'Canceled'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PLACED
    )

    def __str__(self):
        return f"Order {self.id} - Status: {self.get_status_display()}"

    def save(self, *args, **kwargs):
        if self.custom_user and not self.customer:
            self.customer = self.custom_user.name
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} for Order {self.order.id}"
