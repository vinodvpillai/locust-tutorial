# Tutorial 3 — Multiple TaskSets

Demonstrates how to define multiple `TaskSet` classes and assign them all to a single `HttpUser`, letting Locust randomly switch between them during a test run.

## Target API

[http.cat](https://http.cat) — returns a cat image for any HTTP status code.

## Setup

Install dependencies:
```bash
pip install locust
```

## Running the test

```bash
locust -f test/Tutorial_3/testing-using-taskset.py
```

Then open [http://localhost:8089](http://localhost:8089) and configure the number of users and spawn rate.

## What the script does

Two `TaskSet` classes are registered on the same `HttpUser`:

### `MyScript`

| Task | Method | Endpoint | Description |
|---|---|---|---|
| `get_status` | GET | `/status/200` | Fetches the HTTP 200 cat image |

### `MySecondScript`

| Task | Method | Endpoint | Description |
|---|---|---|---|
| `get_random_status` | GET | `/status/<code>` | Picks a random code from `[100, 101, 102, 200, 201, 202]` and fetches that cat image |

Both tasks call `self.interrupt()` after executing, which returns control to the parent `HttpUser` so it can pick the next `TaskSet` from the list.

## Key concepts

- **`TaskSet`** — groups related `@task` methods into a reusable class, separate from `HttpUser`.
- **Multiple TaskSets** — passing a list `tasks = [MyScript, MySecondScript]` lets Locust randomly select a `TaskSet` for each simulated user on every cycle.
- **`self.interrupt()`** — exits the current `TaskSet` and returns control to the parent `HttpUser`. Without it, a simulated user stays inside a `TaskSet` forever and the other `TaskSet` never gets a turn.
- **`self.client` inside `TaskSet`** — delegates to the parent `HttpUser`'s `requests.Session`; all HTTP calls behave the same as in a plain `HttpUser`.
- **`constant(1)`** — each simulated user waits 1 second between tasks.

## Flow diagram

```
HttpUser (MyLoadTest)
├── randomly picks MyScript        → GET /status/200       → interrupt() → back to HttpUser
└── randomly picks MySecondScript  → GET /status/<random>  → interrupt() → back to HttpUser
```

## TaskSet vs plain HttpUser

| | `HttpUser` with `@task` | `HttpUser` with `TaskSet` |
|---|---|---|
| Tasks defined on | The user class itself | One or more separate `TaskSet` classes |
| Best for | Simple, flat task lists | Grouped or nested user flows |
| Switching between groups | Not applicable | Use `self.interrupt()` to return to the parent |
| Reusability | Low | High — a `TaskSet` can be shared across multiple user classes |
