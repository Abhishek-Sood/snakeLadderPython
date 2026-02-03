import random
from logger import logger
class dice:
    def __init__(self, number):
        self.number = random.randint(1, 6)
        logger.info(f"Dice rolled: {self.number}")