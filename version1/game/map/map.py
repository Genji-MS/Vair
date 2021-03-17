from enum import Enum
import numpy as np
import time
import os
import json

POSIBLE_TILES = [1, 2, 3, 4, 5]

BASIC_PROBS = {
    0: np.array([0., 0., 0., 0., 0.]),
    1: np.array([0.005, 0.40, 0.595, 0., 0.]),
    2: np.array([0.005, 0.905, 0.09, 0., 0.]),
    3: np.array([0.005, 0.04, 0.905, 0.05, 0.]),
    4: np.array([0.005, 0., 0.04, 0.905, 0.05]),
    5: np.array([0.005, 0., 0., 0.095, 0.9]),
}


class TileType(Enum):
    no_tile = 0
    rock = 1
    barren = 2
    prairie = 3
    lush_prairie = 4
    forest = 5


class Location:
    def __init__(self, tile_type=None, non_colliding_objects=None, colliding_object=None):
        # Tile type, enum perhaps?
        self.tile = tile_type
        # A list of objects allows for stacking of food / poop potentially
        self.non_colliding_objects = non_colliding_objects
        # An oject too big to move through, Rocks, Players, Enemies
        self.colliding_object = colliding_object

    def will_collision_occur(self):
        return self.colliding_object is not None


class Chunk:
    """
    Generates a map chunk when given the following inputs:

    random_seed = an integer
    id = something unique to identify this PREFER STRING with to make saving and loading chuncks possible.
    probs = a map of tile probabilities
    possible_tiles = a list of possible tiles
    shape = The shape as a tuple (height, width)
    d_con = Distance considered (1, 1) looks in a 3x3 square centered on the location (2, 1) looks in 5x3 rect
    passed_map = an array of tiles that is <= shape
    passed_map_corner = which corner to put the passed map into 1: top left, 2 top right, 3 bottom left, 4 bottom right
    tamper = If set to true may modify the map passed in

    This map generation works stochastically so if we have:

    [barren, barren, prarry] surounding the tile we are genrating we might have:
    barren = [0.5, 0.5, 0] * 2
    prarry = [0.25, 0.5, 0.25]
    or [1.25, 1.5, 0.25] =
       [0.4166, 0.5, 0.0833] probabilities of getting a
       [barren, plain, lush] tile

    , thus making it reliant on existing tiles but more easily extended if we
    wanted a continously generated open world feel.
    """

    def __init__(
        self,
        random_seed,
        id,
        probs=BASIC_PROBS,
        possible_tiles=POSIBLE_TILES,
        shape=(20, 40),
        d_con=(1, 1),
        passed_map=None,
        passed_map_corner=None,
        tamper=False
    ):
        self.random_seed = random_seed
        self.id = id
        self.tile_probabilities = probs
        self.possible_tiles = possible_tiles
        self.shape = shape
        self.distance_considered = d_con
        self.passed_map = passed_map
        self.passed_map_corner = passed_map_corner
        self.tamper = tamper
        self.map = np.zeros(self.shape)
        self.stochastic_gen()
        ...

    def stochastic_gen(self) -> None:
        np.random.seed(self.random_seed)
        self.place_passed_map_if_exists()
        for j in range(self.shape[1]):
            for i in range(self.shape[0]):
                if self.map[i, j] == 0 or self.tamper == True:
                    if i == 0 and j == 0:
                        self.map[0, 0] = np.random.randint(3) + 1
                    else:
                        sum_probs = np.zeros(
                            np.array(self.possible_tiles).shape)
                        count_added_probs = 0
                        for in_i in range(i - self.distance_considered[0], i + self.distance_considered[0] + 1):
                            for in_j in range(j - self.distance_considered[1], j + self.distance_considered[1] + 1):
                                if in_i >= 0 and in_i < self.shape[0] and in_j >= 0 and in_j < self.shape[1]:
                                    # print(f'i: {i} in_i: {in_i} j: {j} in_j: {in_j}')
                                    if self.map[in_i, in_j] != 0:
                                        sum_probs += self.tile_probabilities[self.map[in_i, in_j]]
                                        count_added_probs += 1
                        count_added_probs = 1 if count_added_probs == 0 else count_added_probs
                        # print(sum_probs)
                        actual_probs = sum_probs/count_added_probs
                        # print(actual_probs)
                        # print(sum(actual_probs))
                        self.map[i, j] = np.random.choice(
                            self.possible_tiles, p=actual_probs)
                # print('-----------')
            # print('-----------*******-----------')

    def place_passed_map_if_exists(self) -> None:
        if self.passed_map is not None:
            if self.passed_map_corner is None:
                np.TooHardError(
                    'You forgot to tell me what corner the passed map goes into.')
            if self.passed_map_corner == 1:
                self.map[0:self.passed_map.shape[0],
                         0: self.passed_map.shape[1]] = self.passed_map
            elif self.passed_map_corner == 2:
                self.map[self.shape[0]-self.passed_map.shape[0]:,
                         0: self.passed_map.shape[1]] = self.passed_map
            elif self.passed_map_corner == 3:
                self.map[0:self.passed_map.shape[0],
                         self.shape[1]-self.passed_map.shape[1]:] = self.passed_map
            elif self.passed_map_corner == 4:
                print('4')
                self.map[self.shape[0]-self.passed_map.shape[0]:,
                         self.shape[1]-self.passed_map.shape[1]:] = self.passed_map
            else:
                np.TooHardError(
                    'Passed map corner is an Int from [1, 2, 3, 4]')

    def __str__(self) -> str:
        entire_map = ''
        for row in self.map:
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
            str_row += '\n'
            entire_map += str_row
        return entire_map

    def slice(self, shape) -> np.array:
        return self.map[shape[0]:shape[2], shape[1]: shape[3]]

    def save(self, folder='chunks/') -> str:  # file path
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            folder)
        json_of_chunk = json.dumps({
            'id': self.id,
            'seed': self.random_seed,
            'chunk': [list(array) for array in self.map],
        })
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + self.id + '.json', 'w') as chunk_file:
            chunk_file.write(json_of_chunk)
        return path + self.id + '.json'

    @classmethod
    def load_chunk_from_filepath(cls, file_path):
        with open(file_path) as chunk_file:
            chunk_json = json.load(chunk_file)
            return cls(chunk_json['seed'],
                       chunk_json['id'],
                       passed_map=np.array(chunk_json['chunk']),
                       passed_map_corner=1)


if __name__ == '__main__':
    chunk = Chunk(1, '0')
    print(chunk)
    file_path = chunk.save()
    loaded_chunk = Chunk.load_chunk_from_filepath(file_path)
    print(loaded_chunk)
    """
    for i in range(1, 100):
        time.sleep(.200)
        chunk = Chunk(
            i,
            str(i),
            passed_map=chunk.slice((0, 1, 19, 40)),
            passed_map_corner=2)
        print(chunk)
    """
