import pytest


def test_new_purchase_item(new_purchase_item):
    print(new_purchase_item.product)
    if new_purchase_item.quantity > 0 and "Product" in new_purchase_item.product.name:
        assert True
    else:
        assert False


def test_new_purchase_with_item(new_purchase_with_item):
    print(new_purchase_with_item["purchase"])
    if (
        "Purchase" in new_purchase_with_item["purchase"].name
        and "Product" in new_purchase_with_item["purchase_item"].product.name
    ):
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
