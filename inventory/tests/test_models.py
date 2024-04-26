from django.urls import reverse
from pytest_django.asserts import assertRedirects, assertTemplateUsed
import pytest


def test_new_purchase_item(new_purchase_item):
    print(new_purchase_item.product)
    if new_purchase_item.quantity > 0 and "Product" in new_purchase_item.product.name:
        assert True
    else:
        assert False


# how to check the items
def test_new_purchase_with_items(new_purchase_with_items):
    print(new_purchase_with_items)
    if "Purchase" in new_purchase_with_items.name:
        assert True
    else:
        assert False


def test_new_purchase(new_purchase):
    print(new_purchase)
    if "Purchase" in new_purchase.name:
        assert True
    else:
        assert False


def test_new_brand(new_brand):
    print(new_brand)
    if "Brand" in new_brand.name:
        assert True
    else:
        assert False


def test_new_product_category(new_product_category):
    print(new_product_category)
    if "Category" in new_product_category.name:
        assert True
    else:
        assert False


def test_new_bar_inventory_item(new_bar_inventory_item):
    print(new_bar_inventory_item)
    if "Item" in new_bar_inventory_item.name:
        assert True
    else:
        assert False


def test_new_bar_inventory_product(new_bar_inventory_product):
    print(new_bar_inventory_product)
    if "Product" in new_bar_inventory_product.name:
        assert True
    else:
        assert False


def test_new_purchase_form(client, new_purchase_form):
    form_url = reverse("inventory:purchases_create")
    response = client.post(form_url, data=new_purchase_form)
    print(response.content)
    assert response.status_code == 200


@pytest.mark.parametrize(
    "url_name,template",
    [
        ("inventory:inventory_items", "inventory/item/bar_inventory_items.html"),
        ("inventory:items_create", "inventory/item/bar_inventory_item_form.html"),
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
