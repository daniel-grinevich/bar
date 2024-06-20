from django.db import models
from .fields import HexColorField


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    color = HexColorField(unique=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.CharField(max_length=255)
    items = models.ManyToManyField(
        "MenuItem", related_name="menus", blank=True, null=True
    )

    def get_menu_items(self):
        return self.items.all()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name="menu_items")

    def get_options(self):
        return Option.objects.filter(categories__menu_items=self).select_related(
            "classification"
        )

    def __str__(self):
        return self.name


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


class Classification(models.Model):
    name = models.CharField(max_length=100)
    color = HexColorField(unique=True)

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, related_name="options")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE, related_name="options"
    )

    class Meta:
        ordering = ["name", "classification__name"]

    def __str__(self):
        return self.name
