import json, sys
terminal_values=sys.argv
def Database_search():
    try:
        with open("employees.json","r") as file:
            data=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Failed!,employees.json is either not found or corrupted.")
        sys.exit()
    count=0
    if terminal_values[1]=="search":
        for item in data:
            if item["name"]==terminal_values[2].lower():
                print(f"ID: {item['id']} Name is {item['name']} in {item['department']} department and Salary is {item['salary']}.")
                count+=1
    elif terminal_values[1]=="dept":
        for item in data:
            if item["department"]==terminal_values[2].lower():
                print(f"ID: {item['id']} Name is {item['name']} in {item['department']} department and Salary is {item['salary']}.")
                count+=1
    else:
        for item in data:
            if item["salary"]>=int(terminal_values[2]):
                print(f"ID: {item['id']} Name is {item['name']} in {item['department']} department and Salary is {item['salary']}.")
                count+=1
    if count==0:
        print("No details have found!")
length=len(terminal_values)
if length==3 and (terminal_values[1]=="search" or terminal_values[1]=="dept"):
    Database_search()
elif length==3 and (terminal_values[1]=="min_salary" and terminal_values[2].isdigit()):
    Database_search()
elif length==2 and terminal_values[1]=="search":
    print("Need a employees name to search.")
elif length==2 and terminal_values[1]=="dept":
    print("Need Department name to search.")
elif length==2 and terminal_values[1]=="min_salary":
    print("Need minimum salary to search.")
elif length==1 or length>3:
    print("Invalid values entered!")
else:
    print("Invalid command enter: search / dept / min_salary.")