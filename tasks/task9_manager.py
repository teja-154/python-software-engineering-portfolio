import json, sys
terminal_values=sys.argv
def manage_database():
    try:
        with open("employees.json","r") as file:
            data=json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        print("employees.json file is not found!")
        sys.exit()
    count=0
    changed_data=[]
    if terminal_values[1].lower()=="update":
        for item in data:
            if item["id"]==int(terminal_values[2]):
                item["salary"]=int(terminal_values[3])
                count+=1
        print("Employee salary is updated sucessfully.")
    elif terminal_values[1].lower()=="delete":
        for item in data:
            if item["id"]!=int(terminal_values[2]):
                changed_data.append({"id":item["id"],"name":item["name"],"department":item["department"],"salary":item["salary"]})
            else:
                count+=1
            data=changed_data
        print("Employee data is deleted sucessfully.")
    if count==0:
        print(f"Employee with {terminal_values[2]} was not found!")
        sys.exit()
    with open("employees.json","w") as file:
        json.dump(data,file,indent=4)
length=len(terminal_values)
if length==4 and terminal_values[1]=="update":
    if terminal_values[3].isdigit() and  terminal_values[2].isdigit():
        manage_database()
    else:
        print("Need valid employee values to update")
elif length==3 and terminal_values[1]=="delete":
    if terminal_values[2].isdigit():
        manage_database()
    else:
        print("Need valid employee to delete.")
elif 4>length>1 and (terminal_values[1]=="update" or terminal_values[1]=="delete"):
    print("Not emough employee values.")
else:
    print("Invalid command! Enter: update / delete.")
