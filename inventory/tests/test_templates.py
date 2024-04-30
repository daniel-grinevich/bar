from django.urls import reverse
from pytest_django.asserts import assertRedirects, assertTemplateUsed
import pytest


# Test Template Access
@pytest.mark.parametrize(
    "url_name,template",
    [
        ("inventory:inventory_items", "inventory/item/bar_inventory_items.html"),
        (
            "inventory:inventory_item_create",
            "inventory/item/bar_inventory_item_form.html",
        ),
        ("inventory:purchases", "inventory/purchase/purchases.html"),
        ("inventory:purchases_create", "inventory/purchase/purchase_form.html"),
        ("inventory:brands", "inventory/brand/brands.html"),
        ("inventory:brands_create", "inventory/brand/brand_form.html"),
        ("inventory:categories", "inventory/category/product_categories.html"),
        (
            "inventory:categories_create",
            "inventory/category/product_category_form.html",
        ),
    ],
)
def test_template_access(db, url_name, template, client):
    url = reverse(url_name)
    response = client.get(url)
    assertTemplateUsed(response, template)
    assert response.status_code == 200
