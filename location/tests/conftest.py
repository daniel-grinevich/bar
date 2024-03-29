from pytest_factoryboy import register
from .factories import LocationFactory
import pytest

register(LocationFactory)


@pytest.fixture
def three_locations(db, location_factory):
    return [location_factory() for _ in range(3)]
