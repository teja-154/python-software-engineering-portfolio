---
task_id: 13
date: 2026-09-03
difficulty: Advanced
status: Incomplete
---

# Task 13: FastAPI REST API for Employee Database

## Why a Recruiter Cares
Almost every modern software application—mobile apps, web frontends, microservices—communicates via **REST APIs** (HTTP GET, POST, PUT, DELETE). Knowing how to expose a Python database (like SQLite) through a modern web framework like **FastAPI** with automatic documentation (`/docs`) is one of the most in-demand skills for backend developers and AI engineers building web services.

## Specifications
Create a new Python script named `task13_api.py` that builds a FastAPI web service connected to your `company.db` SQLite database:

1. **FastAPI Application Setup**: 
   * Initialize a FastAPI app instance (`app = FastAPI()`).
2. **GET /employees (List Employees)**: 
   * When accessed via HTTP GET, query `company.db` and return all employee records as a JSON list.
3. **GET /employees/dept/{dept_name} (Filter by Department)**: 
   * Accept a department name in the URL path, query the SQLite database for employees in that department, and return them as JSON.
4. **POST /employees (Add Employee)**: 
   * Accept employee details (`name`, `dept`, `salary`) via JSON request body (using Pydantic models or request parameters), insert the record into `company.db`, and return a success message with the new employee's ID.
5. **Robust Error Handling & Interactive Docs**:
   * Handle database connection errors gracefully.
   * Explore FastAPI's built-in interactive Swagger documentation at `http://127.0.0.1:8000/docs` when the app is running!

## Concepts to Research
* [`fastapi`](https://fastapi.tiangolo.com/) and `uvicorn` (ASGI server to run FastAPI).
* HTTP Methods: `@app.get("/")`, `@app.post("/")`.
* Path parameters (`/items/{item_id}`) and Request Body data (`Pydantic` models or `dict`).

## Self-Verification Checklist
- [ ] **Server Startup**: Run `uvicorn task13_api:app --reload`. Does the server start successfully on port 8000?
- [ ] **Swagger UI Test**: Open `http://127.0.0.1:8000/docs` in your browser. Can you see your API endpoints documented automatically?
- [ ] **GET Test**: Test the `/employees` endpoint via browser or curl. Does it return your SQLite records as JSON?
- [ ] **POST Test**: Use the `/docs` interactive UI to POST a new employee into the database. Does it save successfully?
