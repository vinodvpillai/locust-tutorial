# Tutorial 1 - Locust Basics

Introduces the core building blocks of a Locust test: User classes, tasks, weights, and wait times.

## Concepts Covered

### `User` class
Defines a simulated user. Each class represents a type of user with its own behaviour.

### `@task`
Marks a method as a task Locust will execute. When a user is active, Locust randomly picks one of its `@task` methods to run.

### `weight`
When multiple `User` classes are defined, `weight` controls how often each class is instantiated. Higher weight = more users of that type. Both classes here have `weight = 2`, so they are spawned equally.

### `wait_time = constant(1)`
Introduces a fixed 1-second pause after each task execution, simulating think time between user actions.

## Classes

| Class | Weight | Tasks |
|---|---|---|
| `MyScript` | 2 | `launch`, `search` |
| `MySecondScript` | 2 | `launch`, `search` |

## How to Run

```bash
locust -f test/Tutorial_1/first-test.py
```

When prompted in the Locust UI, use:
- **Number of users:** 4
- **Ramp up:** 4

This ensures both `User` classes get spawned proportionally based on their weights.
