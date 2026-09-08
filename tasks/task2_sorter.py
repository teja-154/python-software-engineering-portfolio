import os
import shutil
from pathlib import Path
import sys

# Target directory: use command line arg if provided, otherwise default to a scratch folder in repo
if len(sys.argv) > 1:
    main_path = Path(sys.argv[1])
else:
    main_path = Path(__file__).parent.parent / "scratch"
    os.makedirs(main_path, exist_ok=True)

Summary=[]
if main_path.exists() and main_path.is_dir():
    files_in_path = list(main_path.iterdir())
    folders=['scripts','notes','misc']
    for folder in folders:
        os.makedirs(main_path / folder, exist_ok=True)
    for item in files_in_path:
        if item.is_file():
            file_name = item.name
            extension = item.suffix
            if extension=='.py':
                shutil.move(str(item), str(main_path / 'scripts' / file_name))
                Summary.append(f'{file_name} is added to scripts')
            elif extension=='.txt':
                shutil.move(str(item), str(main_path / 'notes' / file_name))
                Summary.append(f'{file_name} is added to notes')
            else:
                shutil.move(str(item), str(main_path / 'misc' / file_name))
                Summary.append(f'{file_name} is added to misc')
print(Summary)
