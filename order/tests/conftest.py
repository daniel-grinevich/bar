from pytest_factoryboy import register
import pytest
from .factories import OrderItemFactory, OrderFactory
from recipe.tests.factories import MenuItemFactory, MenuFactory

register(OrderItemFactory)
register(OrderFactory)
register(MenuItemFactory)
register(MenuFactory)


@pytest.fixture
def new_order(db, order_factory):
    return order_factory.build()


@pytest.fixture
def new_order_item(db, order_item_factory):
    return order_item_factory.build()
