import sys, json, csv
terminal_values=sys.argv
def import_converter(file_name):
    try:
        with open(f"{file_name}","r") as file:
            data=list(csv.DictReader(file))
    except(FileNotFoundError):
        print(f"File: '{file_name}' was not found!")
        sys.exit()
    try:
        with open("employees.json","r") as file:
            json_data=list(json.load(file))
        for row in data:
            row["salary"]=int(row["salary"])
            row["id"]=len(json_data)+1
            json_data.append(row)
        with open("employees.json","w") as file:
            json.dump(json_data,file,indent=4)
        print("Conversion completed!")
    except(FileNotFoundError,json.JSONDecodeError,ValueError):
        if ValueError:
            print(f"Invalid salary values in '{file_name}' file should be integer.")
        else:
            print("Conversion failed!, either 'employees.json' was not found or file is corrupt.")
def export_converter(file_name):
    try:
        with open("employees.json","r") as file:
            json_data=json.load(file)
        with open(f"{file_name}.csv","w",newline='') as file:
            fieldnames=["id","name","department","salary"]
            writer=csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(json_data)
        print("Conversion completed!")
    except(FileNotFoundError,json.JSONDecodeError):
        print("Conversion failed!, either 'employees.json' was not found or file is corrupt.")
length=len(terminal_values)
if length==3 and terminal_values[1]=="import":
    import_converter(terminal_values[2])
elif length==3 and terminal_values[1]=="export":
    export_converter(terminal_values[2])
elif length!=3:
    print("Invalid values! try again.")
else:
    print("Need command [import /export] and filename.")