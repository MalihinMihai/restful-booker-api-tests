import pytest

def test_ping(booking_client):
    r = booking_client.ping()
    
    assert r.ok

def test_get_bookings(booking_client):
    r = booking_client.get_bookings()

    #print(r.json())
    
    assert r.ok
    assert isinstance(r.json(), list)


@pytest.mark.parametrize("booking_id", [1, 2, 3])
def test_get_booking_id(booking_client, booking_id):
    r = booking_client.get_booking_id(booking_id)

    print(r.json())

    assert r.ok
    assert isinstance(r.json(), dict)
