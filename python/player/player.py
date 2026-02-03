from logger import logger

class player:
    def __init__ (self, name, position=0):
        self.name = name
        self.position = position
        logger.info(f"Player created: {self.name} at position {self.position}")


def get_players():
    num_players = int(input("Enter number of users: "))
    
    players = []
    for i in range(num_players):
        player_name = input(f"Enter name for Player {i+1}: ")
        players.append(player(player_name))
    return players