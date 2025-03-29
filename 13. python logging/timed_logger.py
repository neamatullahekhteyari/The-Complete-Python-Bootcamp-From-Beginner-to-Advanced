import logging
from logging.handlers import TimedRotatingFileHandler


file_handler = TimedRotatingFileHandler("timed.log", when='M', interval=1 , backupCount=3)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger = logging.getLogger('TimedLogger')
logger.addHandler(file_handler)

import time
for i in range(100):
    logger.info(f"Logging message {i}")
    time.sleep(1)