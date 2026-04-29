# Tutorial 3 — TaskSet

Demonstrates how to use `TaskSet` to organise related tasks into a logical group, separate from the `HttpUser` class.

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

| Task | Method | Endpoint | Description |
|---|---|---|---|
| `get_status` | GET | `/status/200` | Fetches the HTTP 200 cat image and prints a confirmation |

## Key concepts

- **`TaskSet`** — groups a set of `@task` methods into a reusable class. Simulated users execute tasks from the set rather than directly from `HttpUser`. Useful when you want to model a user flow or separate concerns (e.g. auth tasks vs. browsing tasks).
- **`tasks = [MyScript]`** — assigns the `TaskSet` to the `HttpUser`. Locust will pick tasks from `MyScript` during the test run.
- **`self.client` inside `TaskSet`** — transparently delegates to the parent `HttpUser`'s `requests.Session`, so all HTTP calls work the same way as in a plain `HttpUser`.
- **`HttpUser`** — still owns the `host`, `wait_time`, and session; `TaskSet` only groups the task logic.
- **`constant(1)`** — each simulated user waits 1 second between tasks.

## TaskSet vs plain HttpUser

| | `HttpUser` with `@task` | `HttpUser` with `TaskSet` |
|---|---|---|
| Tasks defined on | The user class itself | A separate `TaskSet` class |
| Best for | Simple, flat task lists | Grouped or nested user flows |
| Reusability | Low | High — a `TaskSet` can be shared across multiple user classes |
