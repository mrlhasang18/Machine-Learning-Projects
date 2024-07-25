# this logger file logs the error/exceptions so that they can be easily tracked 
import logging
import os
from datetime import datetime

# LOG file creation
LOG_FILE = F"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#PATH FOR THE LOG FILE
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) 

#Even though there is a folder keep on appending the files inside that
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info("Successfully started loggging!!!")