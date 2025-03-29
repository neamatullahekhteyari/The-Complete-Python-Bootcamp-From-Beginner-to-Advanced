import logging
from logging.handlers import RotatingFileHandler

file_handler = RotatingFileHandler("rotating.log", maxBytes=1024, backupCount=3)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger = logging.getLogger('RotatingLogger')
logger.addHandler(file_handler)

for i in range(100):
    logger.info(f"this is log message {i}")
    
    