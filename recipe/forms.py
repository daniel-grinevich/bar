from django import forms
from .models import Recipe, MenuItem, Menu, Ingredient, Category


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "description", "menu"]


class MenuItemForm(forms.ModelForm):
    menus = forms.ModelMultipleChoiceField(
        queryset=Menu.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta:
        model = MenuItem
        fields = ["name", "description", "price", "categories"]

    def __init__(self, *args, **kwargs):
        super(MenuItemForm, self).__init__(*args, **kwargs)
        self.fields["menus"].queryset = Menu.objects.all()

    def save(self, commit=True):
        menuitem = super().save(commit=False)
        if commit:
            menuitem.save()
        if menuitem.pk:
            menuitem.menus.set(self.cleaned_data["menus"])
            self.save_m2m()
        return menuitem


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["name", "description", "items"]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["quantity", "unit", "recipe"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
