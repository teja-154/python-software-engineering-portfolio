from pathlib import Path
import sys
terminal_values=sys.argv
def parser_file(file_path):
    error=0
    warning=0
    lines=0
    try:
        with open(f"{file_path}","r") as file:
            for line in file:
                lines+=1
                if "ERROR" in line:
                    error+=1
                elif "WARNING" in line:
                    warning+=1
                else:
                    continue
    except FileNotFoundError:
        return "Given file path Doesn't exist in the system."
    return f"Total lines processed are {lines}.\nNo.of 'ERROR' entries found : {error}.\nNo.of 'WARNING' entries found : {warning}."
if len(terminal_values)>1:
    file_path=Path(terminal_values[1])
    if not file_path.is_file():
        print("The path user have given points to a folder or a not-existing file.")
    else:
        print(parser_file(file_path))
else:
    Path("application.log").touch()
    file_path="application.log"
    print(parser_file(file_path))