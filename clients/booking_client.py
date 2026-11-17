from playwright.sync_api import APIRequestContext, APIResponse

class Booking:
    def __init__(self, api: APIRequestContext):
        self.api = api

    def ping(self) -> APIResponse:
        ping = self.api.get("/ping")
        return ping

    def get_bookings(self) -> APIResponse:
        bookings = self.api.get("/booking")
        return bookings

    def get_booking_id(self, booking_id: int) -> APIResponse:
        booking = self.api.get(f"/booking/{booking_id}")
        return booking

    def create_booking(self, payload: dict) -> APIResponse:
        return self.api.post("/booking", data=payload)

    def update_booking(self, booking_id: int, token: str,payload: dict) -> APIResponse:
        headers = {"Cookie": f"token={token}", "Content-Type": "application/json"}
        return self.api.put(f"/booking/{booking_id}", headers=headers, data=payload)

    