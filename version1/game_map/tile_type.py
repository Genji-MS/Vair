from enum import Enum


class TileType(Enum):
    no_tile = '!'
    rock = '\u001b[37m@'
    barren = ' '
    prairie = '\u001b[34m-'
    lush_prairie = '\u001b[36m*'
    forest = '\u001b[32mT'
