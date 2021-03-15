from enum import Enum


class TileType(Enum):
    probability_given_neighbor = {
        0: [0.5, 0.5, 0],
        1: [0.25, 0.5, 0.25],
        2: [0, 0.5, 0.25]
    }
    barren = 0
    prarry = 1
    lush = 2


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
    def __init__(self, height=100, width=100):
        self.arrays = []
