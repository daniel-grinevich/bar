from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Brands(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse("inventory:purchases_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


# Specific Type Product - (ex: 750ml bottle of Titos)
class BarInventoryProduct(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)
    size = models.IntegerField()
    refridgerated = models.BooleanField(default=False)
    brand = models.ForeignKey(Brands, on_delete=models.RESTRICT)
    par_level = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    location = models.ForeignKey("location.Location", on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.RESTRICT)
    purchase_price = models.IntegerField()
    date_purchased = models.DateField()
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(BarInventoryProduct, on_delete=models.RESTRICT)

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
