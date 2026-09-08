import sys, json
from pathlib import Path

terminal_values=sys.argv
emp_path = Path(__file__).parent.parent / "data" / "employees.json"

def employees():
    try:
        with open(emp_path, 'r', encoding="utf-8") as file:
            data=json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        data=[{"id":1,"name":"teja","department":"science","salary":45000},
              {"id":2,"name":"leon","department":"telugu","salary":60000},
              {"id":3,"name":"gray","department":"maths","salary":50000}]
        emp_path.parent.mkdir(parents=True, exist_ok=True)
        with open(emp_path, 'w', encoding="utf-8") as file:
            json.dump(data,file)
    if terminal_values[1]=="add":
        data.append({"id":len(data)+1,"name":terminal_values[2].lower(),"department":terminal_values[3].lower(),"salary":int(terminal_values[4])})
        with open(emp_path, "w", encoding="utf-8") as file:
            json.dump(data,file,indent=4)
        print("Added employee details in file!")
    elif terminal_values[1]=="list":
        print("-----List of Employees-----")
        for item in data:
            print(f"ID : {item['id']} - name is {item['name']} in {item['department']} department and salary is {item['salary']}.")
    else:
        departments={}
        total_salary=0
        if len(data) > 0:
            for item in data:
                total_salary+=item["salary"]
                if item["department"] in departments:
                    departments[item["department"]]+=1
                else:
                    departments[item["department"]]=1
            print(f"Total no.of employees are {len(data)}.\nAverage salary is {total_salary/len(data)}.\nEmployees count per department:\n{departments}")
        else:
            print("No employee records found.")

length=len(terminal_values)
if length==2 and (terminal_values[1]=="list" or terminal_values[1]=="stats"):
    employees()
elif length<2:
    print("Needs command add / list / stats.")
elif length==5 and terminal_values[1]=="add":
    if terminal_values[4].isdigit():
        employees()
    else:
        print("Invalid employee values to add! Enter in these order 'Employee_name Employee_department Employee_salary'.")
elif length!=5 and terminal_values[1]=="add":
    print("Not enough employee values to add.")
else:
    print("Invalid command! Enter add / list / stats.")
