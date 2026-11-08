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