from game.food import Food
from game_map.chunk import Chunk
import os
from shutil import rmtree
# same seed, False, (2,20), (50,50) //same map
# any int, False, (2,20), (50,50)  //new map

# Defualts for production try_too_load_saved_from_seed=False, shape_in_chunks=(2, 20), chunk_shape=(50, 50)
# Defualts for production try_too_load_saved_from_seed=True, shape_in_chunks=(2, 2), chunk_shape=(20, 40)


class GameMap:
    def __init__(self, seed, try_too_load_saved_from_seed=False, shape_in_chunks=(2, 20), chunk_shape=(50, 50)) -> None:
        self.seed = seed
        self.shape = shape_in_chunks
        self.chunk_shape = chunk_shape

        self.chunks = []
        self.populate_chunks_as_none()

        # player value used for Ascii render \u001b[31m
        self.player_value = '\u001b[31mX'
        self.win_location = (0, 20, 0, 20)

        # setting the current chunk
        self.cur_chunk = [shape_in_chunks[0] - 1, shape_in_chunks[1] - 1]
        # setting the player position
        self.player_pos = [45, 45]
        # find position relative to absolute (0,0)
        self.player_pos_relative_to_0_0 = [
            self.cur_chunk[0]*chunk_shape[0] + self.player_pos[0],
            self.cur_chunk[1]*chunk_shape[1] + self.player_pos[1]]

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
            print('Not loading from seed, ')
            print('cleaning up floating chunks, ')

            # alternate less RAM intensive way to gen all chunks, not implemented
            # self.populate_chunks()
            # Simple brute force gen the map
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'chunks/')
            rmtree(path)
            print('generating new map...')
            self.generate_and_split_chunks()
            self.load_chunk(self.cur_chunk[0], self.cur_chunk[1])
        self.move_player((0, 0))

    def has_won(self):
        return self.win_location[0] <= self.player_pos_relative_to_0_0[0] < self.win_location[1] and \
            self.win_location[2] <= self.player_pos_relative_to_0_0[1] < self.win_location[3]

    def set_rel_player_position_to_chunk_and_position(self):
        self.cur_chunk[0] = self.player_pos_relative_to_0_0[0] // self.chunk_shape[0]
        self.cur_chunk[1] = self.player_pos_relative_to_0_0[1] // self.chunk_shape[1]

        self.player_pos[0] = self.player_pos_relative_to_0_0[0] % self.chunk_shape[0]
        self.player_pos[1] = self.player_pos_relative_to_0_0[1] % self.chunk_shape[1]

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

    def unload_all_but_current(self):
        for row in range(len(self.chunks)):
            for chunk_index in range(len(self.chunks[row])):
                if row == self.cur_chunk[0] and chunk_index == self.cur_chunk[1]:
                    pass
                else:
                    if type(self.chunks[row][chunk_index]) is Chunk:
                        self.unload_chunk(row, chunk_index)

    def unload_chunk(self, x, y):
        self.chunks[x][y] = self.chunks[x][y].save()

    def is_move_valid(self, move_vect):
        move_vect = (move_vect[1]*-1, move_vect[0])
        x, y = ((self.player_pos[0] +
                 move_vect[0]) % self.chunk_shape[0]), ((self.player_pos[1] + move_vect[1]) % self.chunk_shape[1])

        relative_to_0_0_x = (self.player_pos_relative_to_0_0[0] +
                             move_vect[0])
        relative_to_0_0_y = (self.player_pos_relative_to_0_0[1] +
                             move_vect[1])
        next_chunk_x = (
            self.player_pos_relative_to_0_0[0] + move_vect[0]) // self.chunk_shape[0]
        next_chunk_y = (
            self.player_pos_relative_to_0_0[1] + move_vect[1]) // self.chunk_shape[1]

        if relative_to_0_0_x < 0 or relative_to_0_0_y < 0 or relative_to_0_0_x >= self.shape[0]*self.chunk_shape[0] or relative_to_0_0_y >= self.shape[1]*self.chunk_shape[1]:
            return False

        return not self.chunks[next_chunk_x][next_chunk_y].map[x][y].will_collision_occur()

    def move_player(self, move_vect):
        move_vect = (move_vect[1]*-1, move_vect[0])
        self.current_chunk().map[self.player_pos[0]
                                 ][self.player_pos[1]].colliding_objects = []
        self.player_pos_relative_to_0_0 = (self.player_pos_relative_to_0_0[0] + move_vect[0],
                                           self.player_pos_relative_to_0_0[1] + move_vect[1])
        self.set_rel_player_position_to_chunk_and_position()
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
        view, case = self.current_chunk().slice_for_render((self.player_pos[0]-2,
                                                            self.player_pos[0]+3,
                                                            self.player_pos[1]-2,
                                                            self.player_pos[1]+3,))
        self.unload_all_but_current()
        if case == 'base':
            return view
        top_left_view = []
        top_view = []
        top_right_view = []
        left_view = []
        center_view = view
        right_view = []
        bottom_left_view = []
        bottom_view = []
        bottom_right_view = []
        if case == 'top left':
            if self.cur_chunk[0] - 1 >= 0 and self.cur_chunk[1] - 1 >= 0:
                self.load_chunk(self.cur_chunk[0] - 1,
                                self.cur_chunk[1] - 1)  # top left
                top_left_view = self.chunks[self.cur_chunk[0] - 1][self.cur_chunk[1] - 1].slice_for_render((
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])-2 + self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])+3 + self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])-2 + self.chunk_shape[1],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])+3 + self.chunk_shape[1],
                ))[0]
        if 'top' in case:
            if self.cur_chunk[0] - 1 >= 0:
                self.load_chunk(
                    self.cur_chunk[0] - 1, self.cur_chunk[1])  # top
                top_view = self.chunks[self.cur_chunk[0] - 1][self.cur_chunk[1]].slice_for_render((
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])-2 + self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])+3 + self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])-2,
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])+3,
                ))[0]
        if case == 'top right':
            if self.cur_chunk[0] - 1 >= 0 and self.cur_chunk[1] + 1 < self.shape[1]:
                self.load_chunk(self.cur_chunk[0] - 1,
                                self.cur_chunk[1] + 1)  # top right
                top_right_view = self.chunks[self.cur_chunk[0] - 1][self.cur_chunk[1] + 1].slice_for_render((
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])-2 + self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])+3 + self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])-2 - self.chunk_shape[1],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])+3 - self.chunk_shape[1],
                ))[0]
        if 'left' in case:
            if self.cur_chunk[1] - 1 >= 0:
                self.load_chunk(self.cur_chunk[0],
                                self.cur_chunk[1] - 1)  # left
                left_view = self.chunks[self.cur_chunk[0]][self.cur_chunk[1] - 1].slice_for_render((
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])-2,
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])+3,
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])-2 + self.chunk_shape[1],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])+3 + self.chunk_shape[1],
                ))[0]
        if 'right' in case:
            if self.cur_chunk[1] + 1 < self.shape[1]:
                self.load_chunk(self.cur_chunk[0], self.cur_chunk[1] + 1)
                right_view = self.chunks[self.cur_chunk[0]][self.cur_chunk[1] + 1].slice_for_render((
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])-2,
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])+3,
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])-2 - self.chunk_shape[1],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])+3 - self.chunk_shape[1],
                ))[0]
        if case == 'bottom left':
            if self.cur_chunk[0] + 1 <= self.shape[0] and self.cur_chunk[1] - 1 >= 0:
                self.load_chunk(self.cur_chunk[0] + 1, self.cur_chunk[1] - 1)
                bottom_left_view = self.chunks[self.cur_chunk[0] + 1][self.cur_chunk[1] - 1].slice_for_render((
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])-2 - self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])+3 - self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])-2 + self.chunk_shape[1],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])+3 + self.chunk_shape[1],
                ))[0]
        if 'bottom' in case:
            if self.cur_chunk[0] + 1 < self.shape[0]:
                self.load_chunk(self.cur_chunk[0] + 1, self.cur_chunk[1])
                bottom_view = self.chunks[self.cur_chunk[0] + 1][self.cur_chunk[1]].slice_for_render((
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])-2 - self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])+3 - self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])-2,
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])+3,
                ))[0]
        if case == 'bottom right':
            if self.cur_chunk[0] + 1 < self.shape[0] and self.cur_chunk[1] + 1 < self.shape[1]:
                self.load_chunk(self.cur_chunk[0] + 1, self.cur_chunk[1] + 1)
                bottom_right_view = self.chunks[self.cur_chunk[0] + 1][self.cur_chunk[1] + 1].slice_for_render((
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])-2 - self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[0] %
                     self.chunk_shape[0])+3 - self.chunk_shape[0],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])-2 - self.chunk_shape[1],
                    (self.player_pos_relative_to_0_0[1] %
                     self.chunk_shape[1])+3 - self.chunk_shape[1],
                ))[0]
        the_top_view = []
        for i in range(len(top_view)):
            if i < len(top_left_view):
                the_top_view += [top_left_view[i]]
            if len(the_top_view) > i:
                the_top_view[i] += top_view[i]
            else:
                the_top_view += [top_view[i]]
            if i < len(top_right_view):
                the_top_view[i] += top_right_view[i]

        the_middle_view = []
        for i in range(len(center_view)):
            if i < len(left_view):
                the_middle_view += [left_view[i]]
            if i < len(the_middle_view):
                the_middle_view[i] += center_view[i]
            else:
                the_middle_view += [center_view[i]]
            if i < len(right_view):
                the_middle_view[i] += right_view[i]
        the_bottom_view = []
        for i in range(len(bottom_view)):
            if i < len(bottom_left_view):
                the_bottom_view += [bottom_left_view[i]]
            if len(the_bottom_view) > i:
                the_bottom_view[i] += bottom_view[i]
            else:
                the_bottom_view += [bottom_view[i]]
            if i < len(bottom_right_view):
                the_bottom_view[i] += bottom_right_view[i]
        for i in the_middle_view:
            the_top_view += [i]
        for i in the_bottom_view:
            the_top_view += [i]
        while len(the_top_view) < 5 and 'bottom' in case:
            the_top_view.append([None]*len(the_top_view[0]))
        while len(the_top_view) < 5 and 'top' in case:
            the_top_view.insert(0, [None]*len(the_top_view[0]))
        while len(the_top_view[0]) < 5 and 'left' in case:
            for i in the_top_view:
                i.insert(0, None)
        while len(the_top_view[0]) < 5 and 'right' in case:
            for i in the_top_view:
                i.append(None)
        return the_top_view

    def render_slice(self):
        # Just renders the view slice
        # print(chr(27) + "[2J")
        print(Chunk(-1, 'not', map=self.return_slice()))
        print('\033[0m')

    def return_slice_as_string(self):
        return str(Chunk(-1, 'not', map=self.return_slice()))


def test():
    game_map = GameMap(seed=0)
    # game_map.render_ascii_map_and_slice()
    print(game_map.return_slice())
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
