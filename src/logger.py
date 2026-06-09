import logging
import os
from datetime import datetime

LOG_FIEL=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FIEL)
os.makedirs(logs_path,exist_ok=True)

LOG_FIEL_PATH=os.path.join(logs_path,LOG_FIEL)
logging.basicConfig(
    filename=LOG_FIEL_PATH,format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s -%(message)s," \
    "level=logging.INFO, ")

if __name__=="__name__":
    logging.info("Logging has started")


 