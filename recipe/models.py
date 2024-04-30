from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    items = models.ManyToManyField("MenuItem", related_name="menus")


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    menu = models.OneToOneField(MenuItem, on_delete=models.CASCADE)


class Ingredient(models.Model):
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )
