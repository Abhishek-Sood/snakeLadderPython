from board.board import board
from dice.dice import dice
from player.player import get_players
from logger import logger


def main():
    def start_game(board, players):
        board.players = players
        for player in board.players:
            player.position = 1

    def move_player(board, player, die_number):
        initial_position = player.position
        player.position += die_number
        if player.position > board.size * board.size:
            player.position = initial_position  # Do not move if exceeds board size
            logger.info(f"{player.name} rolled too high to move from {initial_position}")
            print(f"Next try {player.name}. You rolled too high to move.")

            
        # Check for ladders
        for ladder in board.ladders:
            if player.position == ladder.start:
                print(f"Wow {player.name}. You successfully climbed a ladder!")
                logger.info(f"{player.name} climbed ladder from {ladder.start} to {ladder.end}")
                player.position = ladder.end
        # Check for snakes
        for snake in board.snakes:
            if player.position == snake.head:
                print("Oops, You are bitten by snake and gone down!")
                logger.info(f"{player.name} bitten by snake from {snake.head} to {snake.tail}")
                player.position = snake.tail
        print(f"{player.name} moved to position {player.position}")
        logger.info(f"{player.name} moved from {initial_position} to {player.position}")

    def check_winner(board, player):
        return player.position == board.size * board.size

    game_board = board()
    players = get_players()
    start_game(game_board, players)
    while True:
        for player in players:
            input(f"{player.name}, press enter to roll the dice...")
            logger.info(f"{player.name} is rolling the dice")
            die = dice(0)
            print(f"{player.name}, you rolled a {die.number}")
            move_player(game_board, player, die.number)
            if check_winner(game_board, player):
                print(f"Congratulations {player.name}, you have won the game!")
                logger.info(f"Player {player.name} has won the game!")
                return
            
if __name__ == "__main__":
    main()