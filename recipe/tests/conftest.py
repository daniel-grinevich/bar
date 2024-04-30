from pytest_factoryboy import register
from .factories import MenuItemFactory, MenuFactory
import pytest

register(MenuItemFactory)
register(MenuFactory)


@pytest.fixture
def new_menu(db, menu_factory):
    return MenuFactory.build()


@pytest.fixture
def new_menu_item(db, menu_item_factory):
    return MenuItemFactory.build()
