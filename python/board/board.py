from ladder.ladder import get_ladders
from snake.snake import get_snakes
from config import get_board_size
from logger import logger
import sys

class createboard:
    def __init__ (self,size):
        self.size = size
        self.ladders = get_ladders()
        self.snakes = get_snakes()
        logger.info(f"Board created with size {self.size}, {len(self.ladders)} ladders and {len(self.snakes)} snakes")
    
        for ladder in self.ladders:
            if ladder.start > self.size * self.size or ladder.end > self.size * self.size:
                error_msg = f"Error: Ladder position out of bounds! Start: {ladder.start}, End: {ladder.end}, Board Max: {self.size * self.size}"
                print(error_msg)
                logger.error(error_msg)
                sys.exit(1)  # Exit program

        # Validate snakes
        for snake in self.snakes:
            if snake.head > self.size * self.size or snake.tail > self.size * self.size:
                error_msg = f"Error: Snake position out of bounds! Head: {snake.head}, Tail: {snake.tail}, Board Max: {self.size * self.size}"
                print(error_msg)
                logger.error(error_msg)
                sys.exit(1)  # Exit program


    def displayboard(self):
        print(f"Board Size: {self.size}")

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
