import logging
import os
from datetime import datetime

LOGFILE=f"{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOGFILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOGFILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,

)

