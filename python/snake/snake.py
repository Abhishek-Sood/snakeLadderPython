from logger import logger


class snake: # class for snake 
    def __init__ (self, head, tail): #initialsed the snake with head and tail
        self.head = head
        self.tail = tail
        logger.info(f"Snake created: head at {self.head}, tail at {self.tail}")

def get_snakes():
    try:
        from config import get_snakes_config #import all the snakes from the config file 
    except Exception:
        get_snakes_config = lambda: []  # and made the list empty if error encountered

    snakes_cfg = get_snakes_config() or []
    snakes = [] # empty list of snakes 

    for item in snakes_cfg:
        if isinstance(item, (list, tuple)) and len(item) >= 2: # there should be 2 elements in the list
            head = int(item[0]) # snake head
            tail = int(item[1]) # snake tail
            if head <= tail: #head should be greater than tail if not throw error and log
                logger.error(f"Invalid snake config: head ({head}) must be greater than tail ({tail}) in {item}")
                raise ValueError(f"Invalid snake config: head ({head}) must be greater than tail ({tail}) in {item}")
            snakes.append(snake(head, tail)) # else appended

    logger.info(f"{len(snakes)} snakes created")
    return snakes
