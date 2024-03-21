from pytest_factoryboy import register
from .factories import EventFactory
import pytest

register(EventFactory)


@pytest.fixture
def new_event(db, event_factory):
    event = event_factory.create()
    return event
