## Some of the common functionalities that will be used in project i will be writing here.
import os
import yaml ## for reading yaml files
from src.datascience import logger
import json
## There are two types of library specifically used for model pickling
## 1. pickle 2. joblib   ---> Here we will use joblib(this helps us to probably save the model in some format : .joblib format which is a serialized format)
from ensure import ensure_annotations  ## A amazing decorator that u can use
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError  ## This will help use to handle the exceptions well
import joblib

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:  ## Return type of this function is ConfigBox and the parameter passed to this is Path(we have to specifically give a path)
    ## Here the return type will be ConfigBox so that i will be able to read any keys specifically. Whatever content i m getting in the key.
    """reads yml file and returns

    Args:
        path_to_yml (str): path like input

    Raises:
         ValueError: if yaml file is empty
         e : empty file

    Returns:
          ConfigBox: ConfigBox type         
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file) ## Here u should be able to get the content which will be in the form of key-value pairs and when i apply as ConfigBox on top of it : we should be able to access the keys.
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:  ## If there is a error something related to ValueError then it will be handled by BoxValueError
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e    
## Why using read_yaml : so that i will be able to add any configuration details from my yaml file directly i should be able to call it out.


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool,optional): ignore if multiple directories is to be created. 
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
       path (Path): path to json file
       data (dict): data to be saved in json file
    """ 
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at: {path}") 

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files

    Args:
       path (Path): path to json file

    Returns:
         ConfigBox: data as class attributes instead of dict      
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content) 

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
       data (Any): data to be saved as binary
       path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
       path (Path): path to binary file

    Returns:
       Any: object stored in the file   
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data                   