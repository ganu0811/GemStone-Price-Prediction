import logging
import os
from datetime import datetime


LOG_FILE = f'{datetime.now().strftime("%m_%d_Y_%H_%M_%S")}.log'

log_path = os.path.join(os.getcwd(),'logs')

os.makedirs(log_path,exist_ok=True)


LOG_FILEPATH = os.path.join(log_path,LOG_FILE) 

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
                    )

if __name__ =='main':
    logging.info('This is a test log message')
                    