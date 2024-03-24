from pytest_factoryboy import register
from .factories import CustomUserFactory
import pytest

register(CustomUserFactory)


@pytest.fixture
def new_user1(db, custom_user_factory):
    user = custom_user_factory.create()
    return user
