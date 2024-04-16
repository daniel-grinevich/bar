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
        "product/create/",
        views.CreateBarInventoryProduct.as_view(),
        name="product_create_form",
    ),
    # InventoryItems
    path("items/", views.BarInventoryItemListView.as_view(), name="inventory_items"),
    path(
        "item/create/", views.CreateBarInventoryItem.as_view(), name="item_create_form"
    ),
    # Purchases
    path("purchases/", views.PurchaseListView.as_view(), name="purchases"),
    path("purchases/add/", views.PurchaseCreateView.as_view(), name="purchases_create"),
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
    path("brands/add", views.BrandsCreateView.as_view(), name="brands"),
    # Categories
    path("categories/", views.ProductCategoryListView.as_view(), name="categories"),
    path("categories/add", views.ProductCategoryListView.as_view(), name="categories"),
]
