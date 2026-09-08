import sys, json
def todo():
    try:
        with open("todos.json",'r') as file:
            tasks=json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        tasks=[]
        with open("todos.json",'w') as file:
            json.dump(tasks,file)
    if 'add'==terminal_values[1]:
        tasks.append({'id':f'{len(tasks)+1}','task':f'{terminal_values[2]}','completed':'false'})
    elif 'list'==terminal_values[1]:
        for item in tasks:
            print(item)
    else:
        try:
            if int(terminal_values[2])>len(tasks):
                print(f"the no. of todo's are {len(tasks)}, Select in that range.")
                sys.exit()
        except (TypeError,ValueError):
            print("Enter a Valid Number ID.")
            sys.exit()
        tasks[int(terminal_values[2])-1]['completed']='true'
    with open("todos.json",'w') as file:
        json.dump(tasks,file,indent=4)
terminal_values=sys.argv
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