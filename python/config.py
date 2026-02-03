import json
import os
from math import isqrt

_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

def _load_config():
    try:
        with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def get_board_size():
    cfg = _load_config()
    total = cfg.get("board_size", 100)
    try:
        total = int(total)
    except Exception:
        total = 100
    side = isqrt(total)
    if side * side == total:
        return side
    return total

def get_snakes_config():
    cfg = _load_config()
    return cfg.get("snakes", [])

def get_ladders_config():
    cfg = _load_config()
    return cfg.get("ladders", [])
