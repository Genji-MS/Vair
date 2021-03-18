from .game.food import *
from .map.map import *
from .game_script import game_loop
import os
print(os.getcwd())

# to run cd to Vair then run 'python3 -m version1.map_script'


if __name__ == '__main__':
    print('Basic Test: Print out a chunk')
    chunk = Chunk(1, '0', shape=(20, 40))
    print(chunk)

    print('Map Generation test: Print out many maps')
    for i in range(1, 10):
        time.sleep(.200)
        chunk = Chunk(
            i,
            str(i),
            passed_map=chunk.slice((0, 19, 1, 40)),
            passed_map_corner=3)
        print(chunk)
        print('----------------------------------------------')

    print('Save Test: Print out a saved chunk.')
    file_path = chunk.save()
    loaded_chunk = Chunk.load_chunk_from_filepath(file_path)
    print(loaded_chunk)

    print('Game Map Test: Print out a game map that you can move on.')
    game_loop()
