from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    # InventoryProducts
    path(
        "products/",
        views.BarInventoryProductListView.as_view(),
        name="inventory_products",
    ),
    path(
        "products/create/",
        views.CreateBarInventoryProduct.as_view(),
        name="products_create",
    ),
    # InventoryItems
    path("items/", views.BarInventoryItemListView.as_view(), name="inventory_items"),
    path("items/create/", views.CreateBarInventoryItem.as_view(), name="items_create"),
    # Purchases
    path("purchases/", views.PurchaseListView.as_view(), name="purchases"),
    path(
        "purchases/create/", views.PurchaseCreateView.as_view(), name="purchases_create"
    ),
    path(
        "purchases/<int:pk>/",
        views.PurchaseDetailView.as_view(),
        name="purchases_detail",
    ),
    path(
        "purchases/<int:pk>/item/edit",
        views.PurchaseItemEditView.as_view(),
        name="purchases_item_edit",
    ),
    # Brands
    path("brands/", views.BrandsListView.as_view(), name="brands"),
    path("brands/create/", views.BrandsCreateView.as_view(), name="brands_create"),
    # Categories
    path("categories/", views.ProductCategoryListView.as_view(), name="categories"),
    path(
        "categories/create/",
        views.ProductCategoryListView.as_view(),
        name="categories_create",
    ),
]
