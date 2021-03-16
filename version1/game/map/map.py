from enum import Enum
import random
# import numpy as np
import time
import os
import json

from numpy import tile


class TileType(Enum):
    no_tile = '!'
    rock = '@'
    barren = ' '
    prairie = '-'
    lush_prairie = '*'
    forest = 'T'


POSIBLE_TILES = [TileType.rock, TileType.barren,
                 TileType.prairie, TileType.lush_prairie, TileType.forest]

BASIC_PROBS = {
    TileType.no_tile: [0., 0., 0., 0., 0.],
    TileType.rock: [0.005, 0.40, 0.595, 0., 0.],
    TileType.barren: [0.005, 0.905, 0.09, 0., 0.],
    TileType.prairie: [0.005, 0.04, 0.905, 0.05, 0.],
    TileType.lush_prairie: [0.005, 0., 0.04, 0.905, 0.05],
    TileType.forest: [0.005, 0., 0., 0.095, 0.9],
}


class Location:
    def __init__(self, tile_type=None, non_colliding_objects=None, colliding_objects=None):
        # Tile type, enum perhaps?
        self.tile = tile_type
        # A list of objects allows for stacking of food / poop potentially
        self.non_colliding_objects = non_colliding_objects
        # An oject too big to move through, Rocks, Players, Enemies
        self.colliding_objects = colliding_objects

    def will_collision_occur(self):
        return self.colliding_objects is not None

    def to_json(self):
        return json.dumps({
            'tile': str(self.tile),
            'non_c_o': self.non_colliding_objects,
            'c_o': self.colliding_objects,
        })

    @classmethod
    def from_json(cls, l_json):
        # print(type(l_json))
        return cls(tile_type=TileType[l_json['tile'].split('.')[1]], non_colliding_objects=l_json['non_c_o'], colliding_objects=l_json['c_o'])

    def __str__(self) -> str:
        if self.colliding_objects is not None:
            return self.colliding_objects[0].value
        if self.non_colliding_objects is not None:
            return self.non_colliding_objects[0].value
        return self.tile.value


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
        self.map = []
        for _ in range(shape[0]):
            row = []
            for __ in range(shape[1]):
                row.append(Location(tile_type=TileType.no_tile))
            self.map.append(row)
        self.stochastic_gen()
        ...

    def stochastic_gen(self) -> None:
        random.seed(self.random_seed)
        self.place_passed_map_if_exists()
        for j in range(self.shape[1]):
            for i in range(self.shape[0]):
                if self.map[i][j].tile == TileType.no_tile or self.tamper == True:
                    if i == 0 and j == 0:
                        self.map[0][0].tile = self.possible_tiles[random.randint(
                            0, 4)]
                    else:
                        sum_probs = [0 for _ in range(
                            len(self.possible_tiles))]
                        count_added_probs = 0
                        for in_i in range(i - self.distance_considered[0], i + self.distance_considered[0] + 1):
                            for in_j in range(j - self.distance_considered[1], j + self.distance_considered[1] + 1):
                                if in_i >= 0 and in_i < self.shape[0] and in_j >= 0 and in_j < self.shape[1]:
                                    # print(f'i: {i} in_i: {in_i} j: {j} in_j: {in_j}')
                                    if self.map[in_i][in_j].tile != TileType.no_tile:
                                        sum_probs = [
                                            sum_probs[b] + self.tile_probabilities[self.map[in_i][in_j].tile][b] for b in range(len(sum_probs))]
                                        count_added_probs += 1
                        count_added_probs = 1 if count_added_probs == 0 else count_added_probs
                        # print(sum_probs)
                        actual_probs = [
                            num/count_added_probs for num in sum_probs]
                        # print(actual_probs)
                        # print(sum(actual_probs))
                        # print(actual_probs)
                        # print(self.possible_tiles)
                        self.map[i][j].tile = random.choices(
                            self.possible_tiles, weights=actual_probs)[0]
                # print('-----------')
            # print('-----------*******-----------')

    def place_passed_map_if_exists(self) -> None:
        if self.passed_map is not None:
            if self.passed_map_corner is None:
                TypeError(
                    'You forgot to tell me what corner the passed map goes into.')
            if self.passed_map_corner == 1:
                print('hello')
                for i in range(len(self.passed_map)):
                    for j in range(len(self.passed_map[0])):
                        self.map[i][j] = self.passed_map[i][j]

            elif self.passed_map_corner == 2:
                for i in range(len(self.passed_map)):
                    for j in range(len(self.passed_map[0])):
                        # print(i, j)
                        self.map[i][len(
                            self.map[0]) - len(self.passed_map[0]) + j] = self.passed_map[i][j]

            elif self.passed_map_corner == 3:
                for i in range(len(self.passed_map)):
                    for j in range(len(self.passed_map[0])):
                        # print(i, j)
                        self.map[len(self.map)-len(self.passed_map) +
                                 i][j] = self.passed_map[i][j]

            elif self.passed_map_corner == 4:
                for i in range(len(self.passed_map)):
                    for j in range(len(self.passed_map[0])):
                        # print(i, j)
                        self.map[len(self.map)-len(self.passed_map) + i][len(self.map[0]) -
                                                                         len(self.passed_map[0]) + j] = self.passed_map[i][j]
            else:
                TypeError(
                    'Passed map corner is an Int from [1, 2, 3, 4]')

    def __str__(self) -> str:
        entire_map = ''
        for row in self.map:
            str_row = ''
            for i in row:
                str_row += str(i)
            str_row += '\n'
            entire_map += str_row
        return entire_map

    def slice(self, shape) -> list:
        return [self.map[i][shape[2]: shape[3]] for i in range(shape[0], shape[1])]
        # return self.map[shape[0]:shape[2], shape[1]: shape[3]]

    def save(self, folder='chunks/') -> str:  # file path
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            folder)
        json_of_chunk = json.dumps({
            'id': self.id,
            'seed': self.random_seed,
            'chunk': [[l.to_json() for l in row] for row in self.map],
        })
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + self.id + '.json', 'w') as chunk_file:
            chunk_file.write(json_of_chunk)
        return path + self.id + '.json'

    @ classmethod
    def load_chunk_from_filepath(cls, file_path):
        with open(file_path) as chunk_file:
            chunk_json = json.load(chunk_file)
            chunk_json['chunk'] = [
                [Location.from_json(json.loads(l)) for l in row] for row in chunk_json['chunk']]
            return cls(chunk_json['seed'],
                       chunk_json['id'],
                       passed_map=chunk_json['chunk'],
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
            passed_map=chunk.slice((0, 19, 1, 40)),
            passed_map_corner=3)
        print(chunk)
    """
