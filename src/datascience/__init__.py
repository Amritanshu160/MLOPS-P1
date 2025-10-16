import os
import sys
import logging

## We will be using a generic logging structure
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" ## This is the structure/format : time, levelname(whether its info, warning), module name(like which module the execution is going on , like for eg. i m in my components folder so this module will also be displayed over here), and the message which i want to display in this specific logging.

log_dir = "logs"
log_filepath = os.path.join(log_dir,"logging.log") ## This will be the naming convention i will be using
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)  ## If i m running this entire code in the terminal so i will be able to see the message that i m actually going to put over here inside my file in my output terminal. So that is the reason i m using logging.StreamHandler.
    ]
)
## Initialize it
logger = logging.getLogger("datasciencelogger")

## To test everything is working fine or not
## Continued in main.py