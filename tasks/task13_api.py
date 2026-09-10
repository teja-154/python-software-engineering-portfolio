from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional, Any
from contextlib import asynccontextmanager
import sqlite3

# This part handles the startup and shutdown of our API
@asynccontextmanager
async def Lifespan(app: FastAPI):
    # This runs when we start the server
    print("🚀 Employee API is live and ready for requests!")
    yield
    # This runs when we stop it
    print("Closing the connection with the Database! 🚀")

app = FastAPI(lifespan=Lifespan)
DB_file = "data/company.db" # Database is stored in our data folder

# Initializing the database and creating the table if it's not there
with sqlite3.connect(DB_file, check_same_thread=False) as conn:
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dept TEXT NOT NULL,
    salary REAL CHECK(salary>=0)
    )
    ''')
    conn.commit()

# Helper function to get the database connection
def get_db():
    # check_same_thread=False is needed for FastAPI to work with SQLite
    conn = sqlite3.connect(DB_file, check_same_thread=False)
    conn.row_factory = sqlite3.Row # This makes it return data as dictionaries
    try:
        yield conn
    finally:
        conn.close()

# Pydantic model for our employee data validation
class Employees(BaseModel):
    name: str
    dept: str
    salary: Any # We accept anything here and validate it in our helper

# Helper to check if the salary is valid and positive
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
    return salary_value # Returning the clean float value

# --- API Endpoints ---

@app.get("/")
def server_connection():
    return {"status":"online", "service":"Employee Management API", "database":"connected"}

# Get employees with optional filters for salary and department
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
        return {"Details": "No Employee details found in the database."}
    
    # Converting records to list of dicts for clean JSON output
    return [dict(record) for record in records]

# Get a specific department's employees
@app.get("/employees/dept/{dept_name}")
def get_employee_by_dept(dept_name: str, conn: sqlite3.Connection = Depends(get_db)):
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE dept = ?", (dept_name,))
    records = cur.fetchall()
    return [dict(record) for record in records]

# Add a new employee
@app.post("/employees")
def add_employee_details(employee: Employees, conn: sqlite3.Connection = Depends(get_db)):
    clean_salary = parse_and_validate_salary(employee.salary)
    cur = conn.cursor()
    cur.execute("INSERT INTO employees (name, dept, salary) VALUES (?, ?, ?)", (employee.name, employee.dept, clean_salary))
    conn.commit()
    return {"status": "employee details added!"}

# Update an existing employee's details
@app.put("/employees/{emp_id}")
def updata_employee_details(emp_id: str, employee: Employees, conn: sqlite3.Connection = Depends(get_db)):
    if not emp_id.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid value! Employee id should be an integer."
        )
    
    clean_salary = parse_and_validate_salary(employee.salary)
    cur = conn.cursor()
    cur.execute("UPDATE employees SET name=?, dept=?, salary=? WHERE id=?", (employee.name, employee.dept, clean_salary, int(emp_id)))
    conn.commit()
    
    if cur.rowcount == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Employee id: {emp_id} does not exist in the database."
        )
    return {"status": "Employee details updated successfully!"}

# Delete an employee from the database
@app.delete("/employees/{emp_id}")
def delete_employee_details(emp_id: str, conn: sqlite3.Connection = Depends(get_db)):
    if not emp_id.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid value! Employee id should be an integer."
        )
    
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=?", (int(emp_id),))
    conn.commit()
    
    if cur.rowcount == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Employee id: {emp_id} was not found."
        )
    return {"status": "Employee details have been deleted successfully."}
