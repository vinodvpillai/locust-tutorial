# Tutorial 2 — HttpUser with API Key Authentication

Demonstrates how to use `HttpUser` to load-test a REST API that requires an API key, using environment variables for credential management.

## Target API

[reqres.in](https://reqres.in) — a hosted REST API for testing.

## Setup

1. Ensure a `.env` file exists at the project root with your API key:
   ```
   REQRES_IN_API_KEY=your_api_key_here
   ```

2. Install dependencies:
   ```bash
   pip install locust python-dotenv
   ```

## Running the test

```bash
locust -f test/Tutorial_2/test-using-httpuser.py
```

Then open [http://localhost:8089](http://localhost:8089) and configure the number of users and spawn rate.

## What the script does

| Task | Method | Endpoint | Description |
|---|---|---|---|
| `get_users` | GET | `/api/users` | Fetches the list of users |
| `create_user` | POST | `/api/register` | Registers a new user with a test email and password |

## Key concepts

- **`HttpUser`** — base class that provides a `self.client` (a `requests.Session`) for making HTTP calls.
- **`on_start`** — called once per simulated user on startup; used here to inject the `x-api-key` header into every subsequent request via `self.client.headers.update(...)`.
- **`load_dotenv`** — loads the `.env` file so `environ.get("REQRES_IN_API_KEY")` resolves the API key without hardcoding it.
- **`@task`** — marks a method as a load-test task; Locust picks tasks at random (equal weight by default) during the test run.
- **`constant(1)`** — each simulated user waits 1 second between tasks.
