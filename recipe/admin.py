from django.contrib import admin
from .models import Menu, MenuItem, Recipe, Ingredient, Category

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Ingredient)
