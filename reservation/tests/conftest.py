from pytest_factoryboy import register
from .factories import EventFactory, ReservationFactory
import pytest

register(EventFactory)
register(ReservationFactory)


@pytest.fixture
def new_event(db, event_factory):
    event = event_factory.create()
    return event


@pytest.fixture
def new_reservations(db, reservation_factory):
    reservation_list = []
    for i in range(0, 50):
        reservation_list.append(reservation_factory.create())
    return reservation_list
