from django.urls import path
from .views import (
    MenuListView,
    MenuDetailView,
    MenuCreateView,
    MenuUpdateView,
    MenuDeleteView,
    MenuItemListView,
    MenuItemDetailView,
    MenuItemCreateView,
    MenuItemUpdateView,
    MenuItemDeleteView,
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    IngredientListView,
    IngredientDetailView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
)


app_name = "recipe"

urlpatterns = [
    # Menu URLs
    path("menus/", MenuListView.as_view(), name="menu_list"),
    path("menus/<int:pk>/", MenuDetailView.as_view(), name="menu_detail"),
    path("menus/create/", MenuCreateView.as_view(), name="menu_create"),
    path("menus/<int:pk>/update/", MenuUpdateView.as_view(), name="menu_update"),
    path("menus/<int:pk>/delete/", MenuDeleteView.as_view(), name="menu_delete"),
    # MenuItem URLs
    path("menu-items/", MenuItemListView.as_view(), name="menu_item_list"),
    path("menu-items/<int:pk>/", MenuItemDetailView.as_view(), name="menu_item_detail"),
    path("menu-items/create/", MenuItemCreateView.as_view(), name="menu_item_create"),
    path(
        "menu-items/<int:pk>/update/",
        MenuItemUpdateView.as_view(),
        name="menu_item_update",
    ),
    path(
        "menu-items/<int:pk>/delete/",
        MenuItemDeleteView.as_view(),
        name="menu_item_delete",
    ),
    # Recipe URLs
    path("recipes/", RecipeListView.as_view(), name="recipe_list"),
    path("recipes/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipes/create/", RecipeCreateView.as_view(), name="recipe_create"),
    path("recipes/<int:pk>/update/", RecipeUpdateView.as_view(), name="recipe_update"),
    path("recipes/<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    # Ingredient URLs
    path("ingredients/", IngredientListView.as_view(), name="ingredient_list"),
    path(
        "ingredients/<int:pk>/",
        IngredientDetailView.as_view(),
        name="ingredient_detail",
    ),
    path(
        "ingredients/create/", IngredientCreateView.as_view(), name="ingredient_create"
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient_update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient_delete",
    ),
]
