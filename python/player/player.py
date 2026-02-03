from logger import logger

class player:
    def __init__ (self, name, position=1): # constructor initialized name of player and its position by default 1
        self.name = name
        self.position = position
        logger.info(f"Player created: {self.name} at position {self.position}") # logged player


def get_players():
    num_players = int(input("Enter number of users: "))
    
    players = [] # initial empty list of players will be filled and this function return those players
    for i in range(num_players):
        player_name = input(f"Enter name for Player {i+1}: ")
        players.append(player(player_name))
    return players