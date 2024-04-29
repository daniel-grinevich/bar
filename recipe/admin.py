from django.contrib import admin
from .models import Menu, MenuItem, Recipe, Ingredient

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Recipe)
admin.site.register(Ingredient)
