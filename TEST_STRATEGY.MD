# Test Strategy — Restful-Booker API

## 1. Current Scope & Endpoint Coverage

### `GET /ping` — Healthcheck
* **Checks:** `assert r.status == 201`
* **Rationale:** Confirms API availability before running CRUD tests (fail-fast in CI). Docs header says `200`, while the actual response contract specifies `201 Created` — asserted explicitly against the documented response.

### `GET /booking` — List Bookings
* **Checks:** `assert r.status == 200` and response type is `list`.
* **Rationale:** Validates endpoint availability.

### `GET /booking/{id}` — Read Booking
* **Checks:** `assert r.status == 200` and response type is `dict` (parametrized across IDs `1, 2, 3`).
* **Known Risk & Planned Improvement:** Public DB resets every ~10 minutes, making hardcoded IDs prone to flakiness. Planned migration to the dynamic `created_booking` fixture for full test isolation.

### `POST /booking` — Create Booking
* **Checks:** `assert r.status == 200` and `body["booking"]["firstname"]` matches the sent payload.
* **Rationale:** Critical dependency for downstream operations. Validating body content alongside the documented `200` status code prevents false positives (e.g., `200 OK` returned with corrupted data).

### `PUT /booking/{id}` — Full Update
* **Checks:** `assert r.status == 200` using an authenticated `token` and an isolated `created_booking` fixture.
* **Rationale:** Validates authenticated resource replacement without mutating shared server records.

---

## 2. Architecture & Design Decisions

* **Client Layer (`BookingClient`):** Separates HTTP request execution from test assertions in `tests/api/` for readability and reuse.
* **State Isolation (`yield` fixtures):** Fixtures manage authentication tokens and dynamic booking creation/teardown so tests remain independent.
* **CI/CD Pipeline:** Automated execution on push/PR via GitHub Actions.