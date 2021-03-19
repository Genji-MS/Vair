from enum import Enum


class TileType(Enum):
    no_tile = '!'
    # \u001b[37m
    rock = '@'
    # \u001b[30m
    barren = '|'
    # \u001b[34m
    prairie = '-'
    # \u001b[36m
    lush_prairie = '*'
    # \u001b[32m
    forest = '^'
