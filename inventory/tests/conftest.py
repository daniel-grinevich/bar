from pytest_factoryboy import register
from .factories import (
    BarInventoryItemFactory,
    BarInventoryProductFactory,
    PurchaseItemFactory,
    PurchaseFactory,
    BrandFactory,
    ProductCategoryFactory,
)
from location.tests.factories import LocationFactory
import pytest
from django.forms import formset_factory
from ..forms import (
    PurchaseItemFormSet,
    PurchaseForm,
    BrandForm,
    ProductCategoryForm,
    BarInventoryProductForm,
    BarInventoryItemForm,
)
from ..models import PurchaseItem


register(PurchaseItemFactory)
register(BarInventoryItemFactory)
register(BarInventoryProductFactory)
register(PurchaseFactory)
register(ProductCategoryFactory)
register(BrandFactory)
register(LocationFactory)


# Create Models
@pytest.fixture
def new_purchase_item(db, purchase_item_factory):
    purchase_item = purchase_item_factory.build()
    return purchase_item


@pytest.fixture()
def new_purchase_with_item(db, purchase_factory):
    purchase = purchase_factory.create(with_purchase_items=True)
    purchase_item = PurchaseItemFactory.create(purchase=purchase)
    return {"purchase": purchase, "purchase_item": purchase_item}


@pytest.fixture
def new_purchase(db, purchase_factory):
    purchase = purchase_factory.create()
    return purchase


@pytest.fixture
def new_brand(db, brand_factory):
    brand = brand_factory.build()
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


# Forms


@pytest.fixture
def new_purchase_form():
    form = PurchaseForm({"name": "Purchase A", "date_purchased": "11/11/2023"})
    return form


@pytest.fixture
def new_purchase_form_data():
    return {"name": "Purchase A", "date_purchased": "11/11/2023"}


@pytest.fixture
def new_purchase_item_form_set(db, location_factory, bar_inventory_product_factory):

    location = location_factory.build()
    product = bar_inventory_product_factory.build()
    data = {
        "form-TOTAL_FORMS": "2",
        "form-INITIAL_FORMS": "1",
        "form-0-product": product.pk,
        "form-0-quantity": 1,
        "form-0-purchase_price": 1,
        "form-0-location": location.pk,
        "form-1-product": product.pk,
        "form-1-quantity": 1,
        "form-1-purchase_price": 1,
        "form-1-location": location.pk,
    }
    form_set = PurchaseItemFormSet(data)
    return form_set


@pytest.fixture
def new_brand_form():
    form = BrandForm({"name": "Brand1"})
    return form


@pytest.fixture
def new_brand_form_data():
    return {"name": "Brand1"}


@pytest.fixture
def new_product_category_form():
    form = ProductCategoryForm({"name": "Brand1"})
    return form


@pytest.fixture
def new_product_category_form_data():
    return {"name": "Category1"}


@pytest.fixture
def new_bar_inventory_product_form(
    db, location_factory, brand_factory, product_category_factory
):
    brand = brand_factory.create()
    location = location_factory.create()
    category = product_category_factory.create()
    form = BarInventoryProductForm(
        {
            "name": "Product1",
            "brand": brand.pk,
            "category": category.pk,
            "size": 1,
            "par_level": 5,
            "quantity": 2,
            "location": location.pk,
        }
    )
    return form


@pytest.fixture
def new_bar_inventory_product_form_data(
    db, location_factory, brand_factory, product_category_factory
):
    brand = brand_factory.create()
    location = location_factory.create()
    category = product_category_factory.create()
    return {
        "name": "Product1",
        "brand": brand.pk,
        "category": category.pk,
        "size": 1,
        "par_level": 5,
        "quantity": 2,
        "location": location.pk,
    }


@pytest.fixture
def new_bar_inventory_item_form(db, location_factory, bar_inventory_product_factory):
    location = location_factory.create()
    product = bar_inventory_product_factory.create()
    form = BarInventoryItemForm(
        {
            "name": "Product1",
            "level": 1,
            "date_expired": "12/12/2024",
            "product": product.pk,
            "location": location.pk,
        }
    )
    return form


@pytest.fixture
def new_bar_inventory_item_form_data(
    db, location_factory, bar_inventory_product_factory
):
    location = location_factory.create()
    product = bar_inventory_product_factory.create()
    return {
        "name": "Item1",
        "level": 1,
        "location": location.pk,
        "date_expired": "12/12/2024",
        "product": product.pk,
    }
