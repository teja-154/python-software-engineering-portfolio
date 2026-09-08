from pathlib import Path
import sys
terminal_values=sys.argv
if len(terminal_values)>1:
    folder_path=Path(terminal_values[1])
else:
    folder_path=Path('.').resolve()
if folder_path.is_file():
    print("You have given me an file path, Provide me an folder Path to Analyser through.")
elif folder_path.is_dir():
    with open("report.txt",'w',newline='') as f:
        f.write(f"Analysed Path is {folder_path}.\n")
        total_size=0
        for item in folder_path.iterdir():
            try:
                if item.is_file():
                    size=item.stat().st_size
                    total_size+=size
                    f.write(f"File Name : {item.name} and Size is {size}.\n")
            except PermissionError:
                f.write(f"{item.name} is protected.")
        f.write(f"Total size in this directory is {total_size}.\n")
    print("Path has been Analysed!")
else:
    print("The path you have given does not exist!")
print(terminal_values)