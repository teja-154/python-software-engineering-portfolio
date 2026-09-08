---
task_id: 16
date: 2026-09-05
difficulty: Beginner (Micro-Step)
status: Incomplete
---

# Task 16: Catching SQLite Integrity Errors in FastAPI (Micro-Step)

## Why a Recruiter Cares
When building production APIs, your database has rules (constraints)—like `CHECK(salary >= 0)` or `UNIQUE` names. If a user breaks one of those rules, raw databases throw an ugly internal error that crashes the request or returns a generic 500 Server Error. Professional backend developers catch these database errors (`sqlite3.IntegrityError`) and return a clean, user-friendly `400 Bad Request` HTTP response.

## Specifications
Open your `task13_api.py` and add this simple error guard (takes 15 minutes max):

1. **Catch Integrity Errors on POST / PUT**: 
   * In your `POST /employees` and `PUT /employees/{emp_id}` endpoints, wrap your database `cursor.execute()` and `conn.commit()` inside a `try...except sqlite3.IntegrityError:` block.
   * If an `IntegrityError` occurs (for example, someone tries to insert a negative salary which violates your table's `CHECK(salary >= 0)` constraint), catch it and raise a clean FastAPI `HTTPException`:
     ```python
     raise HTTPException(
         status_code=400, 
         detail="Database constraint violated (e.g. negative salary or invalid data)."
     )
     ```

## Concepts to Research (Use AI if needed!)
* Catching specific exceptions in Python (`except sqlite3.IntegrityError as e:`).
* Raising FastAPI `HTTPException` with status code 400.

## Self-Verification Checklist
- [ ] **Negative Salary Test**: Open your Swagger UI (`/docs`), and try to POST or PUT an employee with a negative salary (e.g., `-1000`). 
- [ ] **Error Check**: Does your API return a clean `400 Bad Request` with your custom error message instead of crashing the server?

---

Your task note has been saved to **`C:/Users/divya/OneDrive/Documents/vs programs/TASKS/Notes/task16_note.md`**.

Keep it simple, test it out, and let me know when you're ready! 🛡️🚀
