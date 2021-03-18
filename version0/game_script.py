from .map.map import *


def game_loop():
    game = GameMap()
    while True:
        player_input = '!'
        game.render_ascii_map()
        while player_input not in 'aAwWsSdD ':
            player_input = input('Use wasd to move: ')
        game.move_player(player_input)
