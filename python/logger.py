import logging
from datetime import datetime
import os


# logger file to collect all the logs in the game 
def create_logger():
    os.makedirs("logs", exist_ok=True)
    log_file = datetime.now().strftime("logs/snake_ladder_%Y-%m-%d_%H-%M-%S.log")
    # file format
    logger = logging.getLogger("SnakeLadderLogger")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file, encoding='utf-8')  #file handler
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("Snake & Ladder Game Session Started")
    return logger

logger = create_logger() 
