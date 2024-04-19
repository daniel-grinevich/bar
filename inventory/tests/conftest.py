from pytest_factoryboy import register
from .factories import (
    BarInventoryItemFactory,
    BarInventoryProductFactory,
    PurchaseItemFactory,
    PurchaseFactory,
    BrandsFactory,
    ProductCategoryFactory,
)
import pytest

register(PurchaseItemFactory)
register(BarInventoryItemFactory)
register(BarInventoryProductFactory)
register(PurchaseFactory)
register(ProductCategoryFactory)
register(BrandsFactory)


@pytest.fixture
def new_purchase_item(db, purchase_item_factory):
    purchase_item = purchase_item_factory.build()
    return purchase_item


@pytest.fixture
def new_purchase_with_items(db, purchase_factory):
    purchase = purchase_factory.build(with_purchase_items=True)
    return purchase


@pytest.fixture
def new_purchase(db, purchase_factory):
    purchase = purchase_factory.build()
    return purchase


@pytest.fixture
def new_brand(db, brands_factory):
    brand = brands_factory.build()
    return brand


@pytest.fixture
def new_product_category(db, product_category_factory):
    category = product_category_factory.build()
    return category


@pytest.fixture
def new_bar_inventory_item(db, bar_inventory_item_factory):
    item = bar_inventory_item_factory.build()
    return item


@pytest.fixture
def new_bar_inventory_product(db, bar_inventory_product_factory):
    product = bar_inventory_product_factory.build()
    return product


@pytest.fixture
def new_purchase_form(db):
    return {"name": "Purchase A"}
