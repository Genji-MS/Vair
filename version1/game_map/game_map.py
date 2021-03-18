from ..game.player import Player
from ..game.food import Food
from .chunk import Chunk


class GameMap:
    def __init__(self) -> None:
        self.chunks = []
        self.player_pos = (15, 5)
        self.player_value = '\u001b[31mX'

        self.current_chunk = 0
        chunk = Chunk(0, '0')
        chunk.map[self.player_pos[0]][self.player_pos[1]
                                      ].colliding_objects = [self.player_value]
        print(chunk)
        self.chunks.append(chunk)

    def is_move_valid(self, move_vect):
        x, y = self.player_pos[0] + \
            move_vect[0], self.player_pos[1] + move_vect[1]
        return not self.chunks[self.current_chunk].map[x][y].will_collision_occur()

    def move_player(self, move_vect):
        self.chunks[self.current_chunk].map[self.player_pos[0]
                                            ][self.player_pos[1]].colliding_objects = []
        self.player_pos = (self.player_pos[0] + move_vect[0],
                           self.player_pos[1] + move_vect[1])
        self.chunks[self.current_chunk].map[self.player_pos[0]][self.player_pos[1]
                                                                ].colliding_objects = [self.player_value]

    def what_food_is_here(self):
        return self.chunks[0].map[self.player_pos[0]][self.player_pos[1]
                                                      ].non_colliding_objects

    def eat_food(self, food_index):
        return self.chunks[0].map[self.player_pos[0]][self.player_pos[1]
                                                      ].remove_food(food_index)

    def create_poop(self,):
        self.chunks[self.current_chunk].map[self.player_pos[0]][self.player_pos[1]].non_colliding_objects.append(
            Food('Poop', 'poop'))

    def render_ascii_map(self):
        # print(chr(27) + "[2J")
        sliced = self.return_slice()
        print(self.chunks[self.current_chunk])
        render_slice_chunk = Chunk(20, '20', shape=(5, 5))
        render_slice_chunk.map = sliced
        print('')
        print(render_slice_chunk)
        print('\033[0m')

    def return_slice(self):
        return self.chunks[self.current_chunk].slice((self.player_pos[0]-2,
                                                      self.player_pos[0]+3,
                                                      self.player_pos[1]-2,
                                                      self.player_pos[1]+3,))


def test():
    game_map = GameMap()
    game_map.render_ascii_map()
    print('should return a list with one food or none with current seed we have one food')
    print(game_map.what_food_is_here())
    print(game_map.create_poop())
    print(game_map.what_food_is_here())
    print(game_map.eat_food(0))
    print(game_map.what_food_is_here())
    print(game_map.is_move_valid((-1, 0)))
    game_map.move_player((-1, 0))
    game_map.render_ascii_map()


if __name__ == '__main__':
    game_map = GameMap()
    game_map.render_ascii_map()
    print(game_map.what_food_is_here())
    print(game_map.create_poop())
    print(game_map.what_food_is_here())
    print(game_map.eat_food(0))
    print(game_map.what_food_is_here())
    game_map.is_move_valid((-1, 0))
    game_map.move_player((-1, 0))
    game_map.render_ascii_map()
