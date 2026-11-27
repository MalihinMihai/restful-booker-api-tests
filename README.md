# Restful-Booker API Testing Framework

API automation framework built with **Python** and **Pytest**, designed around the **API Client pattern** and robust CI/CD integration.

---

## Project Structure

```text
restful-booker-api-tests/
├── clients/          # Dedicated API clients handling HTTP requests (Payloads & Transport)
├── tests/api/        # Test cases, assertions, and test fixtures (conftest.py)
├── .github/workflows # CI/CD automation pipeline (GitHub Actions)
└── TEST_STRATEGY.md  # Detailed test coverage, design decisions, and risk matrix
```

---

## Prerequisites & Installation

Run the following commands in your terminal to set up the local environment:

```bash
# 1. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables
cp .env.example .env 
```

---

## Running Tests

* **Run all tests (standard):**
  ```bash
  pytest
  ```
* **Run with verbose output and print statements (`-s`):**
  ```bash
  pytest -s
  ```

---

## Test Strategy Summary

For a complete breakdown of endpoints, validation criteria, check out the [TEST_STRATEGY.md](TEST_STRATEGY.md) file.
