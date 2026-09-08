import sys, sqlite3
terminal_values=sys.argv
conn=sqlite3.connect("company.db")
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

def add_employee(employee_details):
    cur.execute("INSERT INTO employees(name,dept,salary) VALUES(?,?,?)",(employee_details[0],employee_details[1],employee_details[2]))
    conn.commit()
    print("Added employee details!")
def list_employees():
    cur.execute("SELECT * FROM employees")
    records=cur.fetchall()
    print("List of emoployees:")
    if not records:
        print("No employees data found!")
    for row in records:
        print(f"ID: {row[0]} - Name: {row[1]}, Department: {row[2]}, Salary: {row[3]}.")
def search_by_department(dept):
    cur.execute("SELECT * FROM employees WHERE dept=?",(dept,))
    records=cur.fetchall()
    if not records:
        print("No employees data found!")
    for row in records:
        print(f"ID: {row[0]} - Name: {row[1]}, Department: {row[2]}, Salary: {row[3]}.")
length=len(terminal_values)
if length==5 and terminal_values[1]=="add":
    if terminal_values[4].isdigit():
        if int(terminal_values[4])>=0:            #This line only excutes if number is positive cause isdigit doesn't count negative numbers as integers.
            add_employee(terminal_values[2:])
        else:
            print("Employee salary should not be negative! Enter postive.")
    else:
        print("Invalid salary! should be integer.")
elif length==2 and terminal_values[1]=="list":
    list_employees()
elif length==3 and terminal_values[1]=="search":
    search_by_department(terminal_values[2])
elif length==2 and (terminal_values[1]=="add" or terminal_values[1]=="search"):
    print("Need enough values!")
else:
    print("Invalid! Enter valid command (add/list/search) with valid values.")
conn.close()