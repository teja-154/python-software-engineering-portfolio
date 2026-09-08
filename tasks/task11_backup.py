from datetime import datetime
from pathlib import Path
import json, sys, os, shutil
def create_backup():
    os.makedirs("backups",exist_ok=True)
    file_name=f"employees_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    try:
        with open("employees.json","r") as file:
            json.load(file)
        shutil.copy("employees.json",file_name)
        shutil.move(file_name,"backups")
    except FileNotFoundError:
        print("Backup failed!, the employees file is missing")
        sys.exit()
    except json.JSONDecodeError:
        print("Backup failed!, the employees file is corrupted.")
        sys.exit()
    print("Backup created!")
def list_backups():
    directory="backups"
    if not Path(directory).exists():
        print(f"{directory} does not exits!")
        sys.exit()
    files_in_path=os.listdir(directory)
    for file in files_in_path:
        file=os.path.join(directory,file)
        file_size=os.path.getsize(file)
        print(f"File name: {file}, file size: {file_size} bytes")
def remove_backups(no_of_backups):
    folder=Path("backups")
    if not folder.exists():
        print(f"{folder} does not exits!")
        sys.exit()
    sorted_files=sorted(folder.iterdir(), key=lambda f: f.stat().st_mtime,reverse=True)
    files_to_be_deleted=sorted_files[no_of_backups:]
    for file in files_to_be_deleted:
        try:
            file.unlink()
        except OSError as e:
            print(f"Error deleting {file} :{e}.")
    print("Backups are cleaned!")
terminal_values=sys.argv
length=len(terminal_values)
if length==2 and terminal_values[1]=="backup":
    create_backup()
elif length==2 and terminal_values[1]=="list":
    list_backups()
elif length==3 and terminal_values[1]=="clean":
    if terminal_values[2].isdigit():
        remove_backups(int(terminal_values[2]))
    else:
        print("Need valid no of backups.")
else:
    print("Invalid command! Enter: backup/list/clean.")