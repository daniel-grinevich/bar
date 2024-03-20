from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.FloatField()


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    menu = models.OneToOneField(MenuItem, on_delete=models.CASCADE)


class Ingredient(models.Model):
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
