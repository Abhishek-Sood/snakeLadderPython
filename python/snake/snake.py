from logger import logger


class snake:
    def __init__ (self, head, tail):
        self.head = head
        self.tail = tail
        logger.info(f"Snake created: head at {self.head}, tail at {self.tail}")

def get_snakes():
    try:
        from config import get_snakes_config
    except Exception:
        get_snakes_config = lambda: []

    snakes_cfg = get_snakes_config() or []
    snakes = []

    for item in snakes_cfg:
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            head = int(item[0])
            tail = int(item[1])
            if head <= tail:
                logger.error(f"Invalid snake config: head ({head}) must be greater than tail ({tail}) in {item}")
                raise ValueError(f"Invalid snake config: head ({head}) must be greater than tail ({tail}) in {item}")
            snakes.append(snake(head, tail))

    logger.info(f"{len(snakes)} snakes created")
    return snakes
