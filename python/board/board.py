from ladder.ladder import get_ladders
from snake.snake import get_snakes
from config import get_board_size
from logger import logger


class createboard:
    def __init__ (self,size):
        self.size = size
        self.ladders = get_ladders()
        self.snakes = get_snakes()
        logger.info(f"Board created with size {self.size}x{self.size}, {len(self.ladders)} ladders and {len(self.snakes)} snakes")
    
    
    def displayboard(self):
        print(f"Board Size: {self.size} X {self.size}")

        print("Ladders:")
        for ladder in self.ladders:
            print(f"  Start: {ladder.start}, End: {ladder.end}")
        print("Snakes:")
        for snake in self.snakes:
            print(f"  Head: {snake.head}, Tail: {snake.tail}")

def board():
    size = get_board_size()
    board = createboard(size)
    board.displayboard()
    return board
