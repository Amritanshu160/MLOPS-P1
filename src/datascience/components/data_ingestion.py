import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)

## Data Ingestion Component
class DataIngestion:
    def __init__(self,config:DataIngestionConfig): ## Return type of config will be DataIngestionConfig
        self.config = config ## assigning config
    
    ## Downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(  ## Whe we do url retriever we have to load the data into my local_data_file
                url = self.config.source_URL,
                filename = self.config.local_data_file    ## These are available in config/config.yaml , at this path my entire file will get created
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists")

    ## Extract the zip file
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function retuns None
        """ 
        unzip_path = self.config.unzip_dir ## On this path the entire zip file will be unzipped
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)