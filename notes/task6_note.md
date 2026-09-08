---
task_id: 6
date: 2026-08-28
difficulty: Intermediate
status: Incomplete
---

# Task 6: CLI Todo Item Manager (JSON Persistence)

## Why a Recruiter Cares
Almost every application requires some form of data persistence (saving state so it doesn't disappear when the program closes). Writing a command-line tool that reads, appends, and saves data back to a structured JSON file proves you understand state management, file I/O, and data serialization—core foundations for backend engineering.

## Specifications
Create a Python script (`task6_todo.py`) that acts as a command-line todo list manager using a `todos.json` file for persistence:

1. **Add a Task**: 
   * Command usage: `python task6_todo.py add "Buy groceries"`
   * Should append a new task dictionary `{"id": 1, "task": "Buy groceries", "completed": false}` to `todos.json`. Make sure IDs auto-increment!
2. **List Tasks**: 
   * Command usage: `python task6_todo.py list`
   * Should read `todos.json` and print out all tasks neatly with their status.
3. **Complete a Task**: 
   * Command usage: `python task6_todo.py done 1`
   * Should mark task ID 1 as completed (`true`).
4. **Robust Error Handling**:
   * If `todos.json` doesn't exist when listing or adding, your script should gracefully create it (empty list `[]`) instead of crashing.
   * Handle invalid inputs (e.g., trying to complete an ID that doesn't exist, or missing arguments).

## Concepts to Research
* [`json`](https://docs.python.org/3/library/json.html) module (`json.load()`, `json.dump()`).
* Handling multiple arguments in `sys.argv` (e.g., `sys.argv[1]` for the action like `add`/`list`, and `sys.argv[2]` for the task description or ID).

## Self-Verification Checklist
- [ ] **First Run Test**: Delete `todos.json` and run `python task6_todo.py list`. Does it show an empty list or handle it without crashing?
- [ ] **Add & List Test**: Add two tasks, then run list. Do they both show up with correct IDs?
- [ ] **Completion Test**: Mark one task as done. Does `todos.json` reflect `completed: true` for that task?
