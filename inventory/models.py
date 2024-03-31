from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Brands(models.Model):
    name = models.CharField(max_length=30)


class ProductCategory(models.Model):
    name = models.CharField(max_length=30)


class Purchase(models.Model):
    name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse("inventory:purchases_detail", kwargs={"pk": self.pk})


# Specific Type Product - (ex: 750ml bottle of Titos)
class BarInventoryProduct(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)
    size = models.IntegerField()
    refridgerated = models.BooleanField(default=False)
    brand = models.ForeignKey(Brands, on_delete=models.RESTRICT)
    par_level = models.IntegerField(default=0)


# Item level - one line per 750ml bottle of titos
class BarInventoryItem(models.Model):
    name = models.CharField(max_length=30)
    # location=models.ForeignKey(SpecificLocation, on_delete=models.RESTRICT)
    product = models.ForeignKey(BarInventoryProduct, on_delete=models.RESTRICT)
    level = models.IntegerField(
        default=100, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    purchase_price = models.IntegerField()
    date_purchased = models.DateTimeField()
    date_expired = models.DateField()
    purchase = models.ForeignKey(Purchase, on_delete=models.RESTRICT)
    location = models.ForeignKey("location.Location", on_delete=models.RESTRICT)
