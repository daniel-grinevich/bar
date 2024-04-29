from django import forms
from .models import Recipe, MenuItem, Menu, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "description", "menu"]


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "description", "price"]


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["name", "description", "items"]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["quantity", "unit", "recipe"]
