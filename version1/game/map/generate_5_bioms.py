import numpy as np
from enum import Enum
from my_generator import generate_from_probability
import time


class TileType(Enum):
    no_tile = 0
    rock = 1
    barren = 2
    prairie = 3
    lush_prairie = 4
    forest = 5


def print_map(map):
    for row in map:
        str_row = ''
        for i in row:
            if i == 5:
                str_row += 'T'
            elif i == 4:
                str_row += '*'
            elif i == 3:
                str_row += '-'
            elif i == 2:
                str_row += ' '
            else:
                str_row += '@'
        print(str_row)


if __name__ == '__main__':
    seed = 0
    probs = {
        0: np.array([0., 0., 0., 0., 0.]),
        1: np.array([0.005, 0.40, 0.595, 0., 0.]),
        2: np.array([0.005, 0.905, 0.09, 0., 0.]),
        3: np.array([0.005, 0.04, 0.905, 0.05, 0.]),
        4: np.array([0.005, 0., 0.04, 0.905, 0.05]),
        5: np.array([0.005, 0., 0., 0.095, 0.9]),
    }
    types = [1, 2, 3, 4, 5]
    map = generate_from_probability(seed, (20, 40), probs, types)
    print_map(map)
    for i in range(100):
        time.sleep(.075)
        map = generate_from_probability(
            i % 20, (20, 40), probs, types, passed_map=map[1:, 1:])
        print_map(map)
