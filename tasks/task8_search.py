import json, sys, os

def get_json_path():
    if os.path.exists(os.path.join("data", "employees.json")):
        return os.path.join("data", "employees.json")
    return "employees.json"

terminal_values = sys.argv
def Database_search():
    json_path = get_json_path()
    try:
        with open(json_path, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Failed!, employees.json is either not found or corrupted.")
        sys.exit()
        
    count = 0
    cmd = terminal_values[1].lower()
    query = terminal_values[2].lower()
    
    if cmd == "search":
        for item in data:
            if query in item["name"].lower():
                print(f"ID: {item['id']} Name is {item['name']} in {item['department']} department and Salary is {item['salary']}.")
                count += 1
    elif cmd == "dept":
        for item in data:
            if query in item["department"].lower():
                print(f"ID: {item['id']} Name is {item['name']} in {item['department']} department and Salary is {item['salary']}.")
                count += 1
    elif cmd in ["min_salary", "min-salary"]:
        try:
            min_sal = int(terminal_values[2])
        except ValueError:
            print("Invalid minimum salary value! Should be an integer.")
            sys.exit()
        for item in data:
            if item["salary"] >= min_sal:
                print(f"ID: {item['id']} Name is {item['name']} in {item['department']} department and Salary is {item['salary']}.")
                count += 1
    if count == 0:
        print("No details have found!")

length = len(terminal_values)
if length == 3 and terminal_values[1].lower() in ["search", "dept"]:
    Database_search()
elif length == 3 and (terminal_values[1].lower() in ["min_salary", "min-salary"] and terminal_values[2].isdigit()):
    Database_search()
elif length == 2 and terminal_values[1].lower() == "search":
    print("Need an employee name to search.")
elif length == 2 and terminal_values[1].lower() == "dept":
    print("Need Department name to search.")
elif length == 2 and terminal_values[1].lower() in ["min_salary", "min-salary"]:
    print("Need minimum salary to search.")
elif length == 1 or length > 3:
    print("Invalid values entered!")
else:
    print("Invalid command enter: search / dept / min_salary.")
