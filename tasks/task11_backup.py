from datetime import datetime
from pathlib import Path
import json, sys, os, shutil

def get_json_path():
    if os.path.exists(os.path.join("data", "employees.json")):
        return os.path.join("data", "employees.json")
    return "employees.json"

def create_backup():
    os.makedirs("backups", exist_ok=True)
    json_path = get_json_path()
    file_name = f"employees_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    try:
        shutil.copy(json_path, os.path.join("backups", file_name))
        print("Backup created!")
    except FileNotFoundError:
        print("Backup failed!, the employees file is missing")
        sys.exit()
    except json.JSONDecodeError:
        print("Backup failed!, the employees file is corrupted.")
        sys.exit()

def list_backups():
    directory = "backups"
    if not Path(directory).exists():
        print(f"{directory} does not exist!")
        sys.exit()
    files_in_path = os.listdir(directory)
    if not files_in_path:
        print(f"No backups found in {directory}!")
        sys.exit()
    for file in files_in_path:
        file_path = os.path.join(directory, file)
        file_size = os.path.getsize(file_path)
        print(f"File name: {file}, file size: {file_size} bytes")

def remove_backups(no_of_backups):
    folder = Path("backups")
    if not folder.exists():
        print(f"{folder} does not exist!")
        sys.exit()
    
    sorted_files = sorted(folder.iterdir(), key=lambda f: f.stat().st_mtime, reverse=True)
    if len(sorted_files) <= int(no_of_backups):
        print("No backups to delete.")
        return
    
    files_to_be_deleted = sorted_files[int(no_of_backups):]
    for file in files_to_be_deleted:
        try:
            file.unlink()
        except OSError as e:
            print(f"Error deleting {file} : {e}.")
    print(f"Backups cleaned! Kept {int(no_of_backups)} most recent backups.")

terminal_values = sys.argv
length = len(terminal_values)
if length == 2 and terminal_values[1] == "backup":
    create_backup()
elif length == 2 and terminal_values[1] == "list":
    list_backups()
elif length == 3 and terminal_values[1] == "clean":
    if terminal_values[2].isdigit():
        remove_backups(int(terminal_values[2]))
    else:
        print("Need valid number of backups.")
else:
    print("Invalid command! Enter: backup/list/clean.")
