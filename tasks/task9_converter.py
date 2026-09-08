import sys, json, csv, os

def get_json_path():
    if os.path.exists(os.path.join("data", "employees.json")):
        return os.path.join("data", "employees.json")
    return "employees.json"

terminal_values = sys.argv

def import_converter(file_name):
    try:
        with open(file_name, "r") as file:
            data = list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"File: '{file_name}' was not found!")
        sys.exit()
        
    json_path = get_json_path()
    try:
        with open(json_path, "r") as file:
            json_data = list(json.load(file))
        for row in data:
            row["salary"] = int(row["salary"])
            row["id"] = len(json_data) + 1
            json_data.append(row)
        with open(json_path, "w") as file:
            json.dump(json_data, file, indent=4)
        print("Conversion completed!")
    except FileNotFoundError:
        print("Conversion failed!, 'employees.json' was not found.")
    except json.JSONDecodeError:
        print("Conversion failed!, 'employees.json' file is corrupt.")
    except ValueError:
        print(f"Invalid salary values in '{file_name}' file should be integers.")

def export_converter(file_name):
    json_path = get_json_path()
    try:
        with open(json_path, "r") as file:
            json_data = json.load(file)
        
        # If file_name doesn't end with .csv, or to be safe with user input
        out_file = file_name if file_name.endswith(".csv") else f"{file_name}.csv"
        
        with open(out_file, "w", newline='') as file:
            fieldnames = ["id", "name", "department", "salary"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(json_data)
        print("Conversion completed!")
    except FileNotFoundError:
        print("Conversion failed!, 'employees.json' was not found.")
    except json.JSONDecodeError:
        print("Conversion failed!, 'employees.json' file is corrupt.")

length = len(terminal_values)
if length == 3 and terminal_values[1].lower() == "import":
    import_converter(terminal_values[2])
elif length == 3 and terminal_values[1].lower() == "export":
    export_converter(terminal_values[2])
elif length != 3:
    print("Invalid values! try again.")
else:
    print("Need command [import / export] and filename.")
