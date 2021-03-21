from game.food import Food
from game_map.chunk import Chunk
import os


class GameMap:
    def __init__(self, seed, try_too_load_saved_from_seed=True, shape_in_chunks=(1, 1), chunk_shape=(50, 50)) -> None:
        self.seed = seed
        self.shape = shape_in_chunks
        self.chunk_shape = chunk_shape

        self.chunks = []
        self.populate_chunks_as_none()

        # player value used for Ascii render \u001b[31m
        self.player_value = '\u001b[31mX'

        # setting the current chunk
        self.cur_chunk = (shape_in_chunks[0] - 1, 0)
        # setting the player position
        self.player_pos = (45, 5)
        # find position relative to absolute (0,0)
        self.player_pos_relative_to_0_0 = (
            self.cur_chunk[0]*chunk_shape[0] + self.player_pos[0],
            self.cur_chunk[1]*chunk_shape[1] + self.player_pos[1])

        if try_too_load_saved_from_seed:
            try:
                print('Attempting to load saved files from seed.')
                self.load_chunk(self.cur_chunk[0], self.cur_chunk[1])
                print('Attempting to load saved files from seed worked.')
            except:
                print('Loading from seed failed, generating map')
                # alternate less RAM intensive way to gen all chunks, not implemented
                # self.populate_chunks()
                # Simple brute force gen the map
                self.generate_and_split_chunks()
                self.load_chunk(self.cur_chunk[0], self.cur_chunk[1])
        else:
            print('Not loading from seed, generating map...')
            # alternate less RAM intensive way to gen all chunks, not implemented
            # self.populate_chunks()
            # Simple brute force gen the map
            self.generate_and_split_chunks()
            self.load_chunk(self.cur_chunk[0], self.cur_chunk[1])
        self.move_player((0, 0))

    def current_chunk(self):
        return self.chunks[self.cur_chunk[0]][self.cur_chunk[1]]

    def generate_and_split_chunks(self):
        # Uses a lot of RAM
        shape = self.shape[0] * \
            self.chunk_shape[0], self.shape[1] * self.chunk_shape[1]
        whole_map = Chunk(self.seed, 'whole', shape=shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.chunks[i][j] = Chunk(
                    self.seed,
                    str(hash((self.seed, i, j))),
                    shape=self.chunk_shape,
                    map=whole_map.slice((
                        i*self.chunk_shape[0],
                        i*self.chunk_shape[0] + self.chunk_shape[0],
                        j*self.chunk_shape[1],
                        j*self.chunk_shape[1] + self.chunk_shape[1],
                    ))
                ).save()
        # print(shape)

    def populate_chunks_as_none(self):
        for _ in range(self.shape[0]):
            row = []
            for __ in range(self.shape[1]):
                row.append(None)
            self.chunks.append(row)

    def populate_chunks(self):
        # Uses a lot less RAM
        raise NotImplementedError(
            'Populate chunks would be used to dynamically generate chunks at the beginning of the game.')
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                # print(j)
                if i == 0 and j == 0:
                    self.chunks[self.shape[0] - i - 1][j] = Chunk(
                        self.seed, str(hash((self.seed, i, j))), shape=self.chunk_shape)
                    # print(self.chunks[self.shape[0] - i - 1][j])
                elif i == 0:
                    partial_chunk = self.chunks[
                        self.shape[0] - i - 1][j - 1].slice(
                            (0, self.chunk_shape[0], self.chunk_shape[1]-1, self.chunk_shape[1]))
                    # print('#'*100)
                    # print(self.chunks[self.shape[0] - i - 1][j-1])

                    intermediate = Chunk(
                        self.seed,
                        str(hash((self.seed, i, j))),
                        shape=(self.chunk_shape[0], self.chunk_shape[1] + 1),
                        passed_map=partial_chunk,
                        passed_map_corner=1,
                    )
                    # print('#'*100)
                    # print(intermediate)

                    self.chunks[self.shape[0] - i - 1][j] = Chunk(
                        self.seed,
                        str(hash((self.seed, i, j))),
                        shape=(self.chunk_shape[0], self.chunk_shape[1]),
                        map=intermediate.slice(
                            (0, self.chunk_shape[0], 1, self.chunk_shape[1]+1))
                    )

                    # print('#'*100)
                    # print(self.chunks[self.shape[0] - i - 1][j])
                    self.unload_chunk(self.shape[0] - i - 1, j - 1)
                    if j == self.shape[1] - 1:
                        self.unload_chunk(self.shape[0] - i - 1, j)
                elif j == 0:
                    self.load_chunk(self.shape[0] - i, j)
                    partial_chunk = self.chunks[
                        self.shape[0] - i][j].slice(
                            (self.chunk_shape[0]-1, self.chunk_shape[0], 0, self.chunk_shape[1]))

                    intermediate = Chunk(
                        self.seed,
                        str(hash((self.seed, i, j))),
                        shape=(self.chunk_shape[0], self.chunk_shape[1] + 1),
                        passed_map=partial_chunk,
                        passed_map_corner=4,
                    )

    def load_chunk(self, x, y):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            'chunks/')
        self.chunks[x][y] = Chunk.load_chunk_from_filepath(
            path+str(hash((self.seed, x, y)))+'.json')

    def unload_chunk(self, x, y):
        self.chunks[x][y] = self.chunks[x][y].save()

    def is_move_valid(self, move_vect):
        move_vect = (move_vect[1]*-1, move_vect[0])
        x, y = self.player_pos[0] + \
            move_vect[0], self.player_pos[1] + move_vect[1]
        # print(x, y)
        if x < 0 or y < 0 or x >= self.shape[0]*self.chunk_shape[0] - 1 or y >= self.shape[1]*self.chunk_shape[1] - 1:
            return False

        return not self.current_chunk().map[x][y].will_collision_occur()

    def move_player(self, move_vect):
        move_vect = (move_vect[1]*-1, move_vect[0])
        self.current_chunk().map[self.player_pos[0]
                                 ][self.player_pos[1]].colliding_objects = []
        self.player_pos = (self.player_pos[0] + move_vect[0],
                           self.player_pos[1] + move_vect[1])
        self.current_chunk().map[self.player_pos[0]][self.player_pos[1]].colliding_objects = [
            self.player_value]

    def what_food_is_here(self):
        return self.current_chunk().map[self.player_pos[0]][self.player_pos[1]
                                                            ].non_colliding_objects

    def eat_food(self, food_index):
        return self.current_chunk().map[self.player_pos[0]][self.player_pos[1]
                                                            ].remove_food(food_index)

    def create_poop(self):
        self.current_chunk().map[self.player_pos[0]][self.player_pos[1]].non_colliding_objects.append(
            Food('Poop', 'poop'))

    def render_ascii_map(self):
        print(chr(27) + "[2J")
        print(self.current_chunk())
        print('\033[0m')

    def render_ascii_map_and_slice(self):
        print(chr(27) + "[2J")
        # sliced = self.return_slice()
        print(self.current_chunk())

        print('')
        print(Chunk(-1, 'not', map=self.return_slice()))
        print('\033[0m')

    def return_slice(self):
        # return a regular 2d array of location objects
        # return self.current_chunk().slice_for_render((self.player_pos[0]-2,
        #                                               self.player_pos[0]+3,
        #                                               self.player_pos[1]-2,
        #                                               self.player_pos[1]+3,))
        return self.current_chunk().slice((self.player_pos[0]-2,
                                           self.player_pos[0]+3,
                                           self.player_pos[1]-2,
                                           self.player_pos[1]+3,))

    def render_slice(self):
        # Just renders the view slice
        print(chr(27) + "[2J")
        print(Chunk(-1, 'not', map=self.return_slice()))
        print('\033[0m')

    def return_slice_as_string(self):
        return str(Chunk(-1, 'not', map=self.return_slice()))


def test():
    game_map = GameMap(seed=0)
    game_map.render_ascii_map_and_slice()
    """
    game_map.render_ascii_map_and_slice()
    print('should return a list with one food or none with current seed we have one food')
    print(game_map.what_food_is_here())
    print(game_map.create_poop())
    print(game_map.what_food_is_here())
    print(game_map.eat_food(0))
    print(game_map.what_food_is_here())
    print(game_map.is_move_valid((-1, 0)))
    game_map.move_player((-1, 0))
    game_map.render_ascii_map_and_slice()
    """


if __name__ == '__main__':
    test()
