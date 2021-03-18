import random
import json
from game.food import Food
from game_map.tile_type import TileType

BASIC_FOODPROBS = {
    TileType.rock: [0.75, 0.25, 0., 0.],
    TileType.barren: [1., 0., 0., 0.],
    TileType.prairie: [0.5, 0.1, 0.25, 0.15],
    TileType.lush_prairie: [0.25, 0.1, 0.40, 0.25],
    TileType.forest: [0.4, 0.1, 0.2, 0.3],
}

BASIC_FOOD = [None, 'harmful', 'normal', 'helpful']


class Location:
    def __init__(self, tile_type=None, non_colliding_objects=None, colliding_objects=None, food_probabilities=BASIC_FOODPROBS, food_types=BASIC_FOOD):
        # Tile type, enum perhaps?
        self.tile = tile_type
        # A list of objects allows for stacking of food / poop potentially
        if non_colliding_objects is None:
            self.non_colliding_objects = []
        else:
            self.non_colliding_objects = non_colliding_objects
        # An oject too big to move through, Rocks, Players, Enemies
        if colliding_objects is None:
            self.colliding_objects = []
        else:
            self.colliding_objects = colliding_objects
        self.food_probabilities = food_probabilities
        self.food_types = food_types

    def grow_food(self):
        food = random.choices(
            self.food_types, weights=self.food_probabilities[self.tile])[0]
        if food is not None:
            self.non_colliding_objects = [Food('allthesame', food)]

    def will_collision_occur(self) -> bool:
        return len(self.colliding_objects) > 0

    def to_json(self) -> str:
        return json.dumps({
            'tile': str(self.tile),
            'non_c_o': [item.__dict__ for item in self.non_colliding_objects],
            'c_o': self.colliding_objects,
        })

    def has_food(self):
        for item in self.non_colliding_objects:
            if type(item) == type(Food('', '')):
                return True
        return False

    def remove_food(self, food_index):
        return self.non_colliding_objects.pop(food_index)

    @classmethod
    def from_json(cls, l_json):
        # print(type(l_json))
        cls_object = cls(tile_type=TileType[l_json['tile'].split('.')[
                         1]], non_colliding_objects=l_json['non_c_o'], colliding_objects=l_json['c_o'])
        cls_object.non_colliding_objects = [Food.from_json(
            item) for item in cls_object.non_colliding_objects]
        return cls_object

    def __str__(self) -> str:
        if len(self.colliding_objects) != 0:
            if type(self.colliding_objects[0]) == str:
                return self.colliding_objects[0]
            return self.colliding_objects[0].value
        if len(self.non_colliding_objects) != 0:
            return self.non_colliding_objects[0].value
        return self.tile.value
