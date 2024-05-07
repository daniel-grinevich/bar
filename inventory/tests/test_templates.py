from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
import pytest


# Test Template Access
@pytest.mark.parametrize(
    "url_name,template",
    [
        (
            "inventory:inventory_item_list",
            "inventory/item/bar_inventory_item_list.html",
        ),
        (
            "inventory:inventory_item_create",
            "inventory/item/bar_inventory_item_form.html",
        ),
        ("inventory:purchase_list", "inventory/purchase/purchase_list.html"),
        ("inventory:purchase_create", "inventory/purchase/purchase_form.html"),
        ("inventory:brand_list", "inventory/brand/brand_list.html"),
        ("inventory:brand_create", "inventory/brand/brand_form.html"),
        ("inventory:category_list", "inventory/category/product_category_list.html"),
        (
            "inventory:category_create",
            "inventory/category/product_category_form.html",
        ),
    ],
)
def test_template_access(db, url_name, template, client):
    url = reverse(url_name)
    response = client.get(url)
    assertTemplateUsed(response, template)
    assert response.status_code == 200
