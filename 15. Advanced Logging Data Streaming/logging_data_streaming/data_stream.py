import logging
from logger import log_execution

@log_execution
def stream_log_data(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        logging.error(f"File Not found: {file_path}")