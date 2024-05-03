from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Recipe, MenuItem, Menu, Ingredient
from .forms import (
    RecipeForm,
    MenuForm,
    MenuItemForm,
    IngredientForm,
)  # You'll need to create this form based on the Recipe model


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.pk})


class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.pk})


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipe_list")


class MenuListView(ListView):
    model = Menu
    template_name = "menus/menu_list.html"
    context_object_name = "menus"


class MenuDetailView(DetailView):
    model = Menu
    template_name = "menus/menu_detail.html"


class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = "recipe/menu_create_form.html"

    def get_success_url(self):
        return reverse_lazy("recipe:menu_detail", kwargs={"pk": self.object.pk})


class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = "menus/menu_form.html"

    def get_success_url(self):
        return reverse_lazy("menu_detail", kwargs={"pk": self.object.pk})


class MenuDeleteView(DeleteView):
    model = Menu
    template_name = "menus/menu_confirm_delete.html"
    success_url = reverse_lazy("menu_list")


class MenuItemListView(ListView):
    model = MenuItem
    template_name = "recipe/menu_item_list.html"
    context_object_name = "menu_items"
    paginate_by = 16


class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = "recipe/menu_item_detail.html"


class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "recipe/menu_item_create_form.html"

    def get_success_url(self):
        return reverse_lazy("recipe:menu_item_detail", kwargs={"pk": self.object.pk})


class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "recipe/menu_item_form.html"

    def get_success_url(self):
        return reverse_lazy("menu_item_detail", kwargs={"pk": self.object.pk})


class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = "recipe/menu_item_confirm_delete.html"
    success_url = reverse_lazy("menu_item_list")


class IngredientListView(ListView):
    model = Ingredient
    template_name = "ingredients/ingredient_list.html"
    context_object_name = "ingredients"


class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = "ingredients/ingredient_detail.html"


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/ingredient_form.html"

    def get_success_url(self):
        return reverse_lazy("ingredient_detail", kwargs={"pk": self.object.pk})


class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/ingredient_form.html"

    def get_success_url(self):
        return reverse_lazy("ingredient_detail", kwargs={"pk": self.object.pk})


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "ingredients/ingredient_confirm_delete.html"
    success_url = reverse_lazy("ingredient_list")
