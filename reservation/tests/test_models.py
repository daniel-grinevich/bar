def test_new_event(new_event):
    print(new_event.name)
    assert True


def test_bulk_reservations(new_reservations):
    assert len(new_reservations) == 50
