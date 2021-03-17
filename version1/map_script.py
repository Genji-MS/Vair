from .game.food import *
from .map.map import *
import os
print(os.getcwd())

# to run cd to Vair then run 'python3 -m version1.map_script'


if __name__ == '__main__':
    chunk = Chunk(1, '0', shape=(20, 40))
    print(chunk)
    """
    game_map = GameMap()
    game_map.move_player()
    """
    file_path = chunk.save()
    loaded_chunk = Chunk.load_chunk_from_filepath(file_path)
    print(loaded_chunk)
"""
    for i in range(1, 100):
        time.sleep(.200)
        chunk = Chunk(
            i,
            str(i),
            passed_map=chunk.slice((0, 19, 1, 40)),
            passed_map_corner=3)
        print(chunk)
    """
