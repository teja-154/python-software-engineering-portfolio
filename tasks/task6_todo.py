import sys, json
from pathlib import Path

terminal_values=sys.argv
todo_path = Path(__file__).parent.parent / "data" / "todos.json"

def todo():
    try:
        with open(todo_path, 'r', encoding="utf-8") as file:
            tasks=json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        tasks=[]
        todo_path.parent.mkdir(parents=True, exist_ok=True)
        with open(todo_path, 'w', encoding="utf-8") as file:
            json.dump(tasks,file)
    if len(terminal_values)>1 and 'add'==terminal_values[1]:
        tasks.append({'id':f'{len(tasks)+1}','task':f'{terminal_values[2]}','completed':'false'})
    elif len(terminal_values)>1 and 'list'==terminal_values[1]:
        for item in tasks:
            print(item)
    else:
        try:
            if len(terminal_values)>2 and int(terminal_values[2])>len(tasks):
                print(f"the no. of todo's are {len(tasks)}, Select in that range.")
                sys.exit()
        except (TypeError,ValueError):
            print("Enter a Valid Number ID.")
            sys.exit()
        if len(terminal_values)>2:
            tasks[int(terminal_values[2])-1]['completed']='true'
    with open(todo_path, 'w', encoding="utf-8") as file:
        json.dump(tasks,file,indent=4)

try:
    if len(terminal_values)==2 and terminal_values[1]=='list':
        print("List of items in todo list.")
        todo()
    elif len(terminal_values)==2 and (terminal_values[1]=='done' or terminal_values[1]=='add'):
        print("Enter what to add in the todo list(for 'add') or ID to mark done/completed(for 'done').")
    elif len(terminal_values)>2 and (terminal_values[1]=='done' or terminal_values[1]=='add'):
        todo()
        print("Action completed!")
    else:
        raise IndexError
except IndexError:
    print("Invalid!, Need command add/done/list.")
