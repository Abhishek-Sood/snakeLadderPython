from logger import logger


class ladder:
    def __init__(self, start, end):  # constructor with ladder start and ladder end
        self.start = start
        self.end = end
        logger.info(f"Ladder created: start at {self.start}, end at {self.end}")

def get_ladders():
    try:
        from config import get_ladders_config
    except Exception:
        get_ladders_config = lambda: []

    ladders_cfg = get_ladders_config() or []
    ladders = []

    for item in ladders_cfg:
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            start = int(item[0])
            end = int(item[1])
            if start >= end:
                logger.error(f"Invalid ladder config: start ({start}) must be less than end ({end}) in {item}")
                raise ValueError(f"Invalid ladder config: start ({start}) must be less than end ({end}) in {item}")
            ladders.append(ladder(start, end))

    logger.info(f"Total ladders created: {len(ladders)}")
    return ladders
