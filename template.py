import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = "datascience"

## Below is the folder, file structure we need.
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", ## A constructor __init__.py --> so that we can convert this entire source folder into a package so that it can be imported anywhere.
    ## If i want to import any functionalities into it , this will be imported within the project. I can actually use it anywhere i like , hence inside every folder i create we need this constructor.
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",   ## Any functionality that are generic and are required to be used will be in the utils folder.
    f"src/{project_name}/utils/common.py",    ## Functionalities common to most of the different components i m going to create.
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", ## This will have all the configuration details.
    "params.yaml",  ## Parameters required for machine learning training will be written here.
    "schema.yaml",  ## Reason why we created yaml is that we will be able to read all the configurations from this yaml file.
    "main.py",
    "Dockerfile",
    "setup.py", ## It helps u to create ur entire project as a package.(pypi environment)
    "research/research.ipynb",
    "templates/index.html"
    ## We also require requirements.xt but its already created so not required.
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True) ## exist_ok = True means if file exists do not make it.
        logging.info(f"Creating directory {filedir} for the file : {filename}") ## Some message displayed over here.

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  ## If file path does not exist
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")     

## To create entire project structure open the terminal :
# python template.py command    
# then commit : git add . ---> git commit -m "Project structure"
# then git push origin main (will work only if u created the entire folder with git commands , from github (there u create the repo and copy commands to bring the repo in local)) 
# if u have done the above then when u refresh the github page u will get to see new files which u commited now.       

