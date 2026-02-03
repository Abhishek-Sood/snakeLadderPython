# logger.py
import logging
from datetime import datetime
import os

def create_logger():
    os.makedirs("logs", exist_ok=True)
    log_file = datetime.now().strftime("logs/snake_ladder_%Y-%m-%d_%H-%M-%S.log")

    logger = logging.getLogger("SnakeLadderLogger")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # FileHandler with UTF-8 encoding
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # No console logging (optional)
    # console_handler = logging.StreamHandler()
    # console_handler.setFormatter(formatter)
    # logger.addHandler(console_handler)

    # Use only ASCII-safe message here if needed
    logger.info("Snake & Ladder Game Session Started")  # Removed emojis

    return logger

logger = create_logger()
