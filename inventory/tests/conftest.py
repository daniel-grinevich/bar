from pytest_factoryboy import register
from .factories import (
    BarInventoryItemFactory,
    BarInventoryProductFactory,
    PurchaseItemFactory,
    PurchaseFactory,
    BrandsFactory,
    ProductCategoryFactory,
)
from location.tests.factories import LocationFactory
import pytest
from django.forms import formset_factory
from ..forms import PurchaseItemFormSet
from ..models import PurchaseItem


register(PurchaseItemFactory)
register(BarInventoryItemFactory)
register(BarInventoryProductFactory)
register(PurchaseFactory)
register(ProductCategoryFactory)
register(BrandsFactory)
register(LocationFactory)


@pytest.fixture
def new_purchase_item(db, purchase_item_factory):
    purchase_item = purchase_item_factory.build()
    return purchase_item


@pytest.fixture
def new_purchase_with_item(db, purchase_factory):
    purchase = purchase_factory.create(with_purchase_items=True)
    purchase_item = PurchaseItemFactory.create(purchase=purchase)
    return {"purchase": purchase, "purchase_item": purchase_item}


@pytest.fixture
def new_purchase(db, purchase_factory):
    purchase = purchase_factory.create()
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
def new_purchase_form():
    return {"name": "Purchase A", "date_purchased": "11/11/2023"}


@pytest.fixture
def new_purchase_item_form_set(db, location_factory, bar_inventory_product_factory):

    location = location_factory.build()
    product = bar_inventory_product_factory.build()
    data = {
        "form-TOTAL_FORMS": "2",
        "form-INITIAL_FORMS": "1",
        "form-0-product": product,
        "form-0-quantity": "1",
        "form-0-purchase_price": "1",
        "form-0-location": location,
        "form-1-product": product,
        "form-1-quantity": "1",
        "form-1-purchase_price": "1",
        "form-1-location": location,
    }
    form_set = PurchaseItemFormSet(data)
    return form_set
