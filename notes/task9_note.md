---
task_id: 9
date: 2026-08-31
difficulty: Intermediate
status: Incomplete
---

# Task 9: CLI Employee Record Updater & Deletion Tool (CRUD Completion)

## Why a Recruiter Cares
So far, you have built tools to Create (add), Read (list/search/stats), but true CRUD (Create, Read, Update, Delete) applications require the ability to **modify** existing records (Update) and **remove** records (Delete). In production databases (SQL, MongoDB, REST APIs), handling updates safely without corrupting data or leaving orphan IDs is a fundamental backend engineering competency.

## Specifications
Create a new Python script named `task9_manager.py` that manages updates and deletions for your `employees.json` database:

1. **Update Employee Salary**: 
   * Command usage: `python task9_manager.py update 2 65000`
   * Should locate the employee by ID (`2`) and update their salary to the new value (`65000`), then save back to `employees.json`.
2. **Delete Employee**: 
   * Command usage: `python task9_manager.py delete 3`
   * Should locate the employee by ID (`3`) and remove them entirely from the list, then save back to `employees.json`.
3. **Robust Error Handling**:
   * If the employee ID does not exist, print a clear message (e.g., `"Employee with ID X not found."`) instead of crashing.
   * Handle invalid arguments (e.g., passing letters instead of a numeric ID).
   * Handle missing `employees.json` gracefully.

## Concepts to Research
* Modifying dictionaries inside a Python list by looping through items or matching indices.
* List removal techniques (e.g., filtering out an item using list comprehensions: `data = [emp for emp in data if emp['id'] != target_id]`).
* Type conversion and validation for IDs and updated numeric values.

## Self-Verification Checklist
- [ ] **Update Test**: Update an employee's salary by ID. Open `employees.json` to verify the salary actually changed.
- [ ] **Delete Test**: Delete an employee by ID. Run your list/search tool to verify they are gone.
- [ ] **Missing ID Test**: Try to update or delete an ID that doesn't exist. Does it print an error message instead of crashing?
- [ ] **Invalid Input Test**: Pass text instead of a number for the ID. Does your script handle the `ValueError` cleanly?
