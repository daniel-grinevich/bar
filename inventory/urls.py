from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    # InventoryProducts
    path(
        "products/",
        views.BarInventoryProductListView.as_view(),
        name="inventory_product_list",
    ),
    path(
        "products/create/",
        views.BarInventoryProductCreateView.as_view(),
        name="inventory_product_create",
    ),
    # InventoryItems
    path(
        "items/", views.BarInventoryItemListView.as_view(), name="inventory_item_list"
    ),
    path(
        "items/create/",
        views.BarInventoryItemCreateView.as_view(),
        name="inventory_item_create",
    ),
    path(
        "items/edit/",
        views.BarInventoryItemFormSetView.as_view(),
        name="inventory_item_formset",
    ),
    # Purchases
    path("purchases/", views.PurchaseListView.as_view(), name="purchase_list"),
    path(
        "purchases/create/", views.PurchaseCreateView.as_view(), name="purchase_create"
    ),
    path(
        "purchases/<int:pk>/",
        views.PurchaseDetailView.as_view(),
        name="purchase_detail",
    ),
    path(
        "purchases/<int:pk>/deliver",
        views.deliverPurchase,
        name="purchase_deliver",
    ),
    path(
        "purchases/<int:pk>/item/edit",
        views.PurchaseItemEditView.as_view(),
        name="purchase_item_edit",
    ),
    # Brands
    path("brands/", views.BrandsListView.as_view(), name="brand_list"),
    path("brands/create/", views.BrandCreateView.as_view(), name="brand_create"),
    # Categories
    path("categories/", views.ProductCategoryListView.as_view(), name="category_list"),
    path(
        "categories/create/",
        views.ProductCategoryCreateView.as_view(),
        name="category_create",
    ),
]
