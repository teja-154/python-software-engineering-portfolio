import os
import shutil
main_path="C:/Users/divya/OneDrive/Documents/vs programs/TASKS"
Summary=[]
files_in_path=os.listdir(main_path)
folders=['scripts','notes','misc']
for folder in folders:
    os.makedirs(folder,exist_ok=True)
for item in files_in_path:
    if os.path.isfile(item):
        file_name,extension=os.path.splitext(item)
        if extension=='.py':
            shutil.move(item,'scripts')
            Summary.append(f'{item} is added to scripts')
        elif extension=='.txt':
            shutil.move(item,'notes')
            Summary.append(f'{item} is added to notes')
        else:
            shutil.move(item,'misc')
            Summary.append(f'{item} is added to misc')
print(Summary)