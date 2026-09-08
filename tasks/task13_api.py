from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional, Any
from contextlib import asynccontextmanager
import sqlite3

@asynccontextmanager
async def Lifespan(app: FastAPI):
    print("🚀 Employee API is live and ready for requests!")
    yield
    print("CLosing the connection with the Database! 🚀")

app=FastAPI(lifespan=Lifespan)
DB_file="company.db"

with sqlite3.connect(DB_file) as conn:
    cur=conn.cursor()
    cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dept TEXT NOT NULL,
    salary REAL CHECK(salary>=0)
    )
    '''
    )
    conn.commit()

def get_db():
    conn=sqlite3.connect(DB_file)
    try:
        yield conn
    finally:
        conn.close()

def parse_and_validate_salary(salary: str) -> float:
    try:
        salary_value=float(salary)
    except (ValueError,TypeError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee salary should be an Integer!"
        )
    if salary_value<0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Employee salary should be greater or equal to Zero!"
        )

class Employees(BaseModel):
    name: str
    dept: str
    salary: Any

@app.get("/")
def server_connection():
    return {"status":"online","service":"Employee Management API","database":"connected"}

@app.get("/employees")
def filter_employees(min_salary: Optional[float] = None, dept_name: Optional[str] = None, conn: sqlite3.Connection=Depends(get_db)):
    cur=conn.cursor()
    query="SELECT * FROM employees"
    conditions=[]
    parameters=[]
    if min_salary!=None:
        conditions.append("salary>=?")
        parameters.append(min_salary)
    if dept_name!=None:
        conditions.append("dept=?")
        parameters.append(dept_name)
    if conditions:
        query+=" WHERE "+" AND ".join(conditions)
    cur.execute(query,tuple(parameters))
    records=cur.fetchall()
    if not records:
        return {"Details": "No Employee details found in the database."}
    return [record for record in records]

@app.get("/employees/dept/{dept_name}")
def get_employee_by_dept(dept_name: str, conn: sqlite3.Connection=Depends(get_db)):
    cur=conn.cursor()
    cur.execute("SELECT * FROM employees WHERE dept=?",(dept_name,))
    records=cur.fetchall()
    return records

@app.post("/employees")
def add_employee_details(employee:Employees, conn: sqlite3.Connection=Depends(get_db)):
    clean_salary=parse_and_validate_salary(employee.salary)
    cur=conn.cursor()
    cur.execute("INSERT INTO employees (name,dept,salary) VALUES (?,?,?)",(employee.name,employee.dept,clean_salary))
    conn.commit()
    return {"status":"employee details added!"}

@app.put("/employees/{emp_id}")
def updata_employee_details(emp_id: str, employee: Employees, conn: sqlite3.Connection=Depends(get_db)):
    if not emp_id.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid value! Employee id should be an integer."
        )
    clean_salary=parse_and_validate_salary(employee.salary)
    cur=conn.cursor()
    cur.execute("UPDATE employees SET name=?, dept=?, salary=? WHERE id=?",(employee.name,employee.dept,clean_salary,int(emp_id)))
    conn.commit()
    if cur.rowcount==0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee id: {emp_id} does not exists in the employees database."
        )
    return {"status":"Employee details updated sucessfully!"}

@app.delete("/employees/{emp_id}")
def delete_employee_details(emp_id: str, conn: sqlite3.Connection=Depends(get_db)):
    if not emp_id.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid value! Employee id should be an integer."
        )
    cur=conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=?",(int(emp_id),))
    conn.commit()
    if cur.rowcount==0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee_id: {emp_id} was not found in the employees database."
        )
    return {"status":"Employee details have deleted sucessfully."}
