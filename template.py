import os
from pathlib import Path

project_name = "helmet_detection"

list_of_file = [
    ".github/workflows/.gitkeep"
    "config/config.yaml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/confi_entity.py",
    "notebooks/trials.ipynb",
    "templates/index.html",
    "main.py",
    "app.py",
    "dvc.yaml",
    "params.yaml",
    "setup.py"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    dirname,filename = os.path.split(filepath)
    print(dirname,filename)

    
    if dirname != "":
        os.makedirs(dirname,exist_ok=True)  

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"wb") as f:
            pass
    else:
        print("File Already Exists")