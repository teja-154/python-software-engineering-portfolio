---
task_id: 7
date: 2026-08-29
difficulty: Intermediate
status: Incomplete
---

# Task 7: CLI Employee Database & Salary Analytics

## Why a Recruiter Cares
IT and software roles frequently require managing structured relational datasets, querying records, filtering by criteria, and computing aggregate statistics (e.g., average salary, department breakdowns). Building a mini-database query tool using JSON and Python functions proves you can handle business logic and data aggregation cleanly.

## Specifications
Create a Python script (`task7_employees.py`) that manages an employee database stored in `employees.json`:

1. **Pre-populate or Auto-initialize**: 
   * If `employees.json` doesn't exist, initialize it with at least 3 sample employee dictionaries:
     `{"id": 1, "name": "Alice", "department": "Engineering", "salary": 75000}`
2. **Add Employee**: 
   * Command usage: `python task7_employees.py add "Bob" "Marketing" 60000`
   * Appends a new employee with an auto-incremented ID.
3. **List Employees**: 
   * Command usage: `python task7_employees.py list`
   * Prints all employees nicely formatted.
4. **Department Summary (Analytics)**: 
   * Command usage: `python task7_employees.py stats`
   * Calculates and prints:
     * Total number of employees.
     * Average salary across the company.
     * Breakdown of employee count per department.
5. **Robust Error Handling**:
   * Handle missing files, invalid numbers for salary (catch `ValueError`), and missing arguments.

## Concepts to Research
* Aggregations and loops over lists of dictionaries.
* Dictionaries as frequency counters (e.g., counting employees per department using a lookup dictionary: `dept_counts[dept] = dept_counts.get(dept, 0) + 1`).
* Parsing integers/floats from terminal arguments (`int()`, `float()`).

## Self-Verification Checklist
- [ ] **First Run Test**: Delete `employees.json` and run `python task7_employees.py list`. Does it auto-populate or handle initialization gracefully?
- [ ] **Add & Stats Test**: Add a couple of employees across different departments, then run `stats`. Are the averages and counts calculated correctly?
- [ ] **Error Test**: Pass a non-number for salary (e.g. `python task7_employees.py add "Charlie" "HR" "abc"`). Does it catch the error and exit gracefully?
