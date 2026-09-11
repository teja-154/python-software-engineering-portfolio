from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional, Any
from contextlib import asynccontextmanager
import sqlite3

# This handles what happens when the API starts and stops
@asynccontextmanager
async def Lifespan(app: FastAPI):
    print("🚀 Employee API is live and ready for requests!")
    yield
    print("Closing the connection with the Database! 🚀")

app = FastAPI(lifespan=Lifespan)
DB_file = "data/company.db" # Database is stored in our data folder

# Initializing the database and creating our two tables
with sqlite3.connect(DB_file, check_same_thread=False) as conn:
    cur = conn.cursor()
    # 1. Employees Table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dept TEXT NOT NULL,
    salary REAL CHECK(salary>=0)
    )
    ''')
    # 2. Departments Table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    budget INTEGER NOT NULL
    )
    ''')
    conn.commit()

# Helper to get the DB connection
def get_db():
    conn = sqlite3.connect(DB_file, check_same_thread=False)
    conn.row_factory = sqlite3.Row # Returns results as dictionaries
    try:
        yield conn
    finally:
        conn.close()

# Helper to check if a department actually exists
def department_exists(dept_name: str, conn: sqlite3.Connection) -> bool:
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM departments WHERE name = ?", (dept_name,))
    result = cur.fetchone()
    return result[0] > 0

# Helper to validate and clean salary input
def parse_and_validate_salary(salary: Any) -> float:
    try:
        salary_value = float(salary)
    except (ValueError, TypeError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee salary should be a valid number!"
        )
    if salary_value < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Employee salary! Should be greater or equal to Zero!"
        )
    return salary_value

# Data model for employee requests
class Employees(BaseModel):
    name: str
    dept: str
    salary: Any

# --- Endpoints ---

@app.get("/")
def server_connection():
    return {"status":"online", "service":"Employee Management API", "database":"connected"}

# List and Filter Employees
@app.get("/employees")
def filter_employees(min_salary: Optional[float] = None, dept_name: Optional[str] = None, conn: sqlite3.Connection = Depends(get_db)):
    cur = conn.cursor()
    query = "SELECT * FROM employees"
    conditions = []
    parameters = []
    
    if min_salary != None:
        conditions.append("salary >= ?")
        parameters.append(min_salary)
    if dept_name != None:
        conditions.append("dept = ?")
        parameters.append(dept_name)
    
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    
    cur.execute(query, tuple(parameters))
    records = cur.fetchall()
    
    if not records:
        return {"Details": "No matching employees found."}
    
    return [dict(record) for record in records]

# Add a new employee (Now with department check!)
@app.post("/employees")
def add_employee_details(employee: Employees, conn: sqlite3.Connection = Depends(get_db)):
    clean_salary = parse_and_validate_salary(employee.salary)
    
    # Check if the department is real before adding
    if not department_exists(employee.dept, conn):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Department '{employee.dept}' not found. Create the department first!"
        )
    
    cur = conn.cursor()
    cur.execute("INSERT INTO employees (name, dept, salary) VALUES (?, ?, ?)", (employee.name, employee.dept, clean_salary))
    conn.commit()
    return {"status": "employee details added!"}

# List all departments
@app.get("/departments")
def list_departments(conn: sqlite3.Connection = Depends(get_db)):
    cur = conn.cursor()
    cur.execute("SELECT id, name, budget FROM departments ORDER BY name")
    return [dict(record) for record in cur.fetchall()]

# Add a new department
@app.post("/departments")
def add_new_department(dept_name: str, budget: int, conn: sqlite3.Connection = Depends(get_db)):
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO departments (name, budget) VALUES (?, ?)", (dept_name, budget))
        conn.commit()
        return {"status": "Department added!", "id": cur.lastrowid}
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Department '{dept_name}' already exists!"
        )

# Update employee
@app.put("/employees/{emp_id}")
def updata_employee_details(emp_id: str, employee: Employees, conn: sqlite3.Connection = Depends(get_db)):
    if not emp_id.isdigit():
        raise HTTPException(status_code=400, detail="ID must be an integer.")
    
    clean_salary = parse_and_validate_salary(employee.salary)
    
    # Also check department here for safety
    if not department_exists(employee.dept, conn):
        raise HTTPException(status_code=400, detail="Department not found.")

    cur = conn.cursor()
    cur.execute("UPDATE employees SET name=?, dept=?, salary=? WHERE id=?", (employee.name, employee.dept, clean_salary, int(emp_id)))
    conn.commit()
    
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Employee not found.")
    return {"status": "Updated successfully!"}

# Delete employee
@app.delete("/employees/{emp_id}")
def delete_employee_details(emp_id: str, conn: sqlite3.Connection = Depends(get_db)):
    if not emp_id.isdigit():
        raise HTTPException(status_code=400, detail="ID must be an integer.")
    
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=?", (int(emp_id),))
    conn.commit()
    
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Employee not found.")
    return {"status": "Deleted successfully."}
