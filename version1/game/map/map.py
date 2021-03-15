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
    """
    There are two ways I can think of to generate the landscape, one would be to
    generate the land based on surounding tiles so like if we have tiles:
    [barren, barren, prarry] surounding the tile we are genrating we woul have:
    barren = [0.5, 0.5, 0] * 2
    prarry = [0.25, 0.5, 0.25]
    or [1.25, 1.5, 0.25] = 
       [0.4166, 0.5, 0.0833] probabilities of getting a
       [barren, plain, lush] tile

    , thus making it reliant on existing
    tiles but more easily extended if we wanted a continous open world feel.
    The way to do it would be to generate a smooth depth map sort of thing using
    numpy and then using the depth to determine what the tile is, this could make
    the generation time faster but might make it difficulte to make the different
    sections of the map's bioms line up when crossing "chunk" borders.

    """

    def __init__(self, height=100, width=100):
        self.arrays = []
        ...
