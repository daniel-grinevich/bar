from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ("ordered", "Ordered"),
    ("sent", "Sent"),
    ("delivered", "Delivered"),
    ("cancelled", "Cancelled"),
)


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ordered")
    date_purchased = models.DateField(default=date.today)
    expected_delivery_date = models.DateField(null=True, blank=True)
    date_delivered = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("inventory:purchases_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    # Called to update quantity changes caused by the delivery status being updated
    def updatePurchaseItemDelivery(self):
        for purchaseItem in self.purchaseitem_set.all():
            product = BarInventoryProduct.objects.get(pk=purchaseItem.product.pk)
            # If changed to delivered, add quantity. If changed back, subtract quantity
            if self.status == "delivered":
                product.quantity = product.quantity + purchaseItem.quantity
            else:
                product.quantity = product.quantity - purchaseItem.quantity
                if product.quantity < 0:
                    product.quantity = 0
            product.save()

    def save(self, *args, **kwargs):
        # if updating - delivered should not be allowed to be set unless you are updating the purchase.
        if self.id:
            old_value = Purchase.objects.get(pk=self.id)
            if self.status != old_value.status and (
                self.status == "delivered" or old_value.status == "delivered"
            ):
                self.updatePurchaseItemDelivery()

        super().save(*args, **kwargs)


# Specific Type Product - (ex: 750ml bottle of Titos)
class BarInventoryProduct(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)
    size = models.PositiveIntegerField()
    refridgerated = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)
    par_level = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    location = models.ForeignKey("location.Location", on_delete=models.RESTRICT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.RESTRICT)
    purchase_price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(BarInventoryProduct, on_delete=models.RESTRICT)
    location = models.ForeignKey("location.Location", on_delete=models.RESTRICT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.purchase.name} : {self.product.name}"


# Item level - one line per 750ml bottle of titos
class BarInventoryItem(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey(BarInventoryProduct, on_delete=models.RESTRICT)
    level = models.IntegerField(
        default=100, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    date_expired = models.DateField()
    location = models.ForeignKey("location.Location", on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.name} : {self.product.name}"
