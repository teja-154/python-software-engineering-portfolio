---
task_id: 8
date: 2026-08-30
difficulty: Intermediate-Advanced
status: Incomplete
---

# Task 8: CLI Employee Database Search & Filter (Query Engine)

## Why a Recruiter Cares
In Tasks 6 and 7, you learned how to load JSON, add items, list them, and compute basic statistics. Real-world applications, however, require *querying* data—such as searching for specific records by name or filtering items based on conditional criteria (e.g., finding all employees in the "Engineering" department or those earning above a certain salary). This bridges the gap between simple script writing and building mini database query engines.

## Specifications
Expand or build upon your dataset logic (`employees.json`) in a new script named `task8_search.py`:

1. **Search by Name**: 
   * Command usage: `python task8_search.py search "teja"`
   * Should perform a case-insensitive search for any employee whose name contains the query string and print their details neatly.
2. **Filter by Department**: 
   * Command usage: `python task8_search.py dept "Science"`
   * Should filter and display all employees belonging to that specific department.
3. **Filter by Minimum Salary**: 
   * Command usage: `python task8_search.py min-salary 50000`
   * Should filter and display all employees whose salary is greater than or equal to the specified amount.
4. **Robust Error Handling**:
   * Handle missing `employees.json` gracefully (inform the user there are no records or auto-initialize).
   * Handle missing arguments (e.g., if the user types `python task8_search.py search` without a name, catch it and print a helpful usage guide).
   * Handle invalid salary numbers (catch `ValueError` if someone inputs text instead of a number for `min-salary`).

## Concepts to Research
* List comprehensions or filtering loops in Python (`[emp for emp in data if ...]`).
* Case-insensitive string matching (`.lower()`, `in`).
* Multi-argument `sys.argv` routing (checking `sys.argv[1]` for the command, and `sys.argv[2]` for the filter query/value).

## Self-Verification Checklist
- [ ] **Search Test**: Search for a partial name (e.g. `ej` in `teja`). Does it match correctly?
- [ ] **Department Filter Test**: Filter by a valid department and an invalid department. Does it display the correct matches or an empty state message?
- [ ] **Salary Filter Test**: Filter by `min-salary`. Does it correctly exclude employees below that threshold?
- [ ] **Missing Argument Test**: Run `python task8_search.py search` with no search term. Does it exit cleanly with an explanation instead of crashing?
