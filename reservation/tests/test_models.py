def test_new_event(new_event):
    print(new_event.name)
    assert True


def test_bulk_reservations(new_reservations):
    assert len(new_reservations) == 50


def test_reservation_event_relationship(new_event, new_reservation):
    new_reservation.event = new_event
    print(new_reservation.event.name)
    print(new_event.name)
    assert new_reservation.event.name == new_event.name
