---
task_id: 14
date: 2026-09-04
difficulty: Advanced
status: Incomplete
---

# Task 14: Complete CRUD API with PUT, DELETE & Query Parameters

## Why a Recruiter Cares
A real-world backend API must support the full **CRUD lifecycle**: Create, Read, Update, and Delete. In your Task 13, you built the foundation (Create + Read). Today, you are completing the API by adding **Update (PUT)** and **Delete** operations, plus introducing **query parameters** for filtering. This mirrors how production REST APIs work in companies like Zomato, Swiggy, Razorpay, and even large MNCs.

## Specifications
Expand your existing `task13_api.py` FastAPI application to include the following:

1. **PUT /employees/{emp_id} (Update Employee)**: 
   * Accept an employee ID in the URL path and updated details (`name`, `dept`, `salary`) in the request body.
   * Find the employee by ID in `company.db`, update their fields, and return the updated record.
   * If the ID does not exist, return a clear `404 Not Found` error.

2. **DELETE /employees/{emp_id} (Delete Employee)**: 
   * Accept an employee ID in the URL path.
   * Delete the record from `company.db` and return a success message.
   * If the ID does not exist, return a clear `404 Not Found` error.

3. **GET /employees with Query Parameters (Advanced Filtering)**: 
   * Modify your existing `/employees` endpoint to accept optional query parameters:
     * `?min_salary=50000` → only return employees with salary >= 50000
     * `?department=Engineering` → only return employees in that department
   * Allow combining both filters (`/employees?department=Engineering&min_salary=75000`).

4. **Improved Error Handling**: 
   * Return proper HTTP status codes (`200 OK`, `201 Created`, `404 Not Found`, `400 Bad Request`).
   * Use FastAPI's `HTTPException` for clean error responses.

## Concepts to Research
* FastAPI path parameters (`/employees/{emp_id}`) and query parameters (`?min_salary=...`).
* Pydantic models for request bodies (`EmployeeUpdate` model).
* SQL `UPDATE` and `DELETE` statements with `WHERE id = ?`.
* HTTP status codes (`status.HTTP_200_OK`, `status.HTTP_201_CREATED`, `status.HTTP_404_NOT_FOUND`).
* `cursor.lastrowid` vs `rowcount` in SQLite.

## Self-Verification Checklist
- [ ] **PUT Test**: Update an employee's salary by ID. Verify the database reflects the change.
- [ ] **DELETE Test**: Delete an employee by ID. Verify they are removed from subsequent GET requests.
- [ ] **404 Test**: Try to update/delete an ID that doesn't exist. Does it return a proper 404 JSON error?
- [ ] **Query Filter Test**: Call `/employees?min_salary=60000`. Does it filter correctly? What about combining `?department=Engineering&min_salary=80000`?
- [ ] **Swagger UI Test**: Visit `/docs` and test all endpoints from the interactive UI. Do the status codes and responses look correct?

---

## 💡 Interview Tip
When you put this on your resume or GitHub, you can say:
*"I designed and implemented a production-style REST API using FastAPI and SQLite, supporting full CRUD operations, parameterized SQL queries, input validation with Pydantic, and advanced query filtering. The API includes proper HTTP status codes and error handling."*

This single sentence covers 80% of what backend interviewers look for in freshers.

Your task note has been saved to **`C:/Users/divya/OneDrive/Documents/vs programs/TASKS/Notes/task14_note.md`**.

Build it, test it, and let me know when you're ready for review! 🚀
