import pyglet as py
import sprites
import game.health as Thlay
import game.poops as Hraka
import game.stomach as Flay
import game_map.game_map as World


world = World.GameMap(0)
thlay = Thlay.Health()
hraka = Hraka.Poops()
flay = Flay.Stomach(hraka, thlay)
pos_x, pos_y = world.player_pos
world_slice = world.return_slice()
tiles = []
# for y in range(5):
#     col = []
#     for x in range(5):
#         tile = world_slice[x][y]


def anchor_center(image):
    """set the anchor point of an image to its center"""
    image.anchor_x = image.width//2
    image.anchor_y = image.height//2


vair = sprites.Sprite_Rabbit()
for image in vair.img_seq:
    anchor_center(image)
py.clock.schedule_interval(vair.update, 0.07)

window = py.window.Window()
# bg_color = py.shapes.Rectangle(0,0,window.width, window.height, color=(22, 78, 22))
batch_bg = py.graphics.Batch()
batch_stats = py.graphics.Batch()
BUFFER = 8  # padding
STATS_BUFFER = 66
stats_border = py.shapes.Rectangle((BUFFER//2)-1, window.height - (75+1) - (BUFFER//2), 120+2, 74+2, color=(255, 255, 255), batch=batch_bg)
stats_fill = py.shapes.Rectangle(BUFFER//2, window.height - 75 - (BUFFER//2), 120, 74, color=(0, 0, 0), batch=batch_bg)
health_txt = py.text.Label('Thlay', x=BUFFER + 3, y=window.height - 20 - BUFFER, batch=batch_stats)
stomach_txt = py.text.Label('Flay', x=BUFFER + 12, y=window.height - 40 - BUFFER, batch=batch_stats)
poops_txt = py.text.Label('Hraka', x=BUFFER, y=window.height - 60 - BUFFER, batch=batch_stats)
health_val = py.text.Label(thlay.get_stats(), x= STATS_BUFFER, y=health_txt.y, batch=batch_stats)
stomach_val = py.text.Label(flay.get_stats(), x= STATS_BUFFER, y=stomach_txt.y, batch=batch_stats)
poops_val = py.text.Label(hraka.get_stats(), x = STATS_BUFFER, y=poops_txt.y, batch=batch_stats)


@window.event
def on_draw():
    window.clear()
    # bg_color.draw()
    batch_bg.draw()
    batch_stats.draw()
    vair.sprite.draw()


@window.event
def on_key_press(symbol, modifiers):
    if not vair.animating:  # ensure no animations are active before receiving input
        if symbol == py.window.key.SPACE:  # eat food
            food_menu = world.what_food_is_here()
            if food_menu.len:
                # create list of foods and send input with #keys, checking that eating is True while the food menu is displayed
                vair.nom()  # start the eating animation while player selects from the menu
        # input to rest/skip a turn & foods menu
        if hraka.poopsAvailable():  # check if we are able to move
            # set defaults
            hop_dir = 'X'
            hop_side = 'X'
            hop_target = [0, 0]
            # project movement
            if symbol == py.window.key.Q:
                hop_dir = 'out'
                hop_side = 'L'
                hop_target[0] -= 1
            elif symbol == py.window.key.A:
                hop_dir = 'in'
                hop_side = 'L'
                hop_target[0] -= 1
                hop_target[1] -= 1
            elif symbol == py.window.key.E:
                hop_dir = 'out'
                hop_side = 'R'
                hop_target[0] += 1
                hop_target[1] += 1
            elif symbol == py.window.key.D:
                hop_dir = 'in'
                hop_side = 'R'
                hop_target[0] += 1
            elif symbol == py.window.key.W:
                hop_dir = 'out'
                hop_target[1] += 1
            elif symbol == py.window.key.S:
                hop_dir = 'in'
                hop_target[1] -= 1
            # check if projected position is valid
            if world.is_move_valid(hop_target):
                hraka.make_poop() #decriment poops
                world.create_poop() #put a poop into the map
                if hop_dir == 'in':
                    vair.hop_in(hop_side)
                else:
                    vair.hop_out(hop_side)
                world.move_player(hop_target)
                py.clock.schedule_once(on_anim_complete, 0.6)


def on_anim_complete(_):
    flay.update()
    health_val.text = thlay.get_stats()
    stomach_val.text = flay.get_stats()
    poops_val.text = hraka.get_stats()
    if thlay.is_alive() == False:
        pass
        # call end game
    #update graphics to be drawn
    world.render_slice()
    world_slice = world.return_slice()


if __name__ == '__main__':
    py.app.run()
