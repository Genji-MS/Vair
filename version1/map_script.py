from .game.food import *
from .map.map import *
import os
print(os.getcwd())

if __name__ == '__main__':
    chunk = Chunk(1, '0', shape=(20, 40))
    print(chunk)
