import pytest

def test_ping(booking_client):
    r = booking_client.ping()
    
    assert r.status == 201

def test_get_bookings(booking_client):
    r = booking_client.get_bookings()
    
    assert r.status == 200
    assert isinstance(r.json(), list)


@pytest.mark.parametrize("booking_id", [1, 2, 3])
def test_get_booking_id(booking_client,booking_id):
    r = booking_client.get_booking_id(booking_id)

    print(r.json())
    assert r.status == 200
    assert isinstance(r.json(), dict)

def test_create_booking(booking_client,booking_payload):

    r = booking_client.create_booking(booking_payload)
    print("Status Code: ", r.status)
    print("Response Body: ", r.text())
    
    assert r.status == 200
    body = r.json()    
    assert body["booking"]["firstname"] == booking_payload["firstname"]

def test_update_booking(booking_client, booking_payload, token, created_booking):
    
    updated_payload = booking_payload.copy()
    updated_payload["totalprice"] = 200

    r = booking_client.update_booking(booking_id=created_booking, token=token, payload=updated_payload)

    assert r.status == 200
    body = r.json()
    assert body["totalprice"] == updated_payload["totalprice"]
s