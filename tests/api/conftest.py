from dotenv import load_dotenv

load_dotenv()

import os
import pytest

from clients.booking_client import Booking


@pytest.fixture(scope="session")
def api(playwright):
    ctx = playwright.request.new_context(
    base_url=os.getenv("API_URL", "https://restful-booker.herokuapp.com"),
    #extra_http_headers={ "Accept": "application/json", "Content-Type": "application/json",},
    )

    yield ctx
    ctx.dispose()

@pytest.fixture(scope="session")
def token(api):
    r = api.post("/auth", data={
        "username": os.environ["API_USER"],
        "password": os.environ["API_PASSWORD"],
    })
    body = r.json()
    assert "token" in body, f"Autentificare esuata: {body}"
    return body["token"]

@pytest.fixture
def booking_client(api) -> Booking:
    return Booking(api)
