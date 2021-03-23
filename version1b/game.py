import pyglet as py
import sprites
import game.health as Thlay
import game.poops as Hraka
import game.stomach as Flay
import game_map.game_map as World


world = World.GameMap(4)
thlay = Thlay.Health()
hraka = Hraka.Poops()
flay = Flay.Stomach(hraka, thlay)
pos_x, pos_y = world.player_pos
world_slice = world.return_slice()
menu = []


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
MENU_BUFFER = 24  # padding
MENU_WIDTH = 120
MENU_HEIGHT = 74
stats_border = py.shapes.Rectangle((MENU_BUFFER)-1, 0 + (MENU_HEIGHT//2+2) - MENU_BUFFER, MENU_WIDTH+2, MENU_HEIGHT+2, color=(255, 255, 255), batch=batch_bg)
stats_fill = py.shapes.Rectangle(stats_border.x +1, stats_border.y +1, MENU_WIDTH, MENU_HEIGHT, color=(0, 0, 0), batch=batch_bg)
stats_txt = py.text.Label('STATS', x=stats_border.x + stats_border.width//2-30, y=stats_border.y + stats_border.height + 4, bold=True, color=(0,180,20,255), batch=batch_bg)
food_border = py.shapes.Rectangle(window.width - stats_border.x - stats_border.width, window.height - (MENU_HEIGHT+2) - (MENU_BUFFER), MENU_WIDTH+2, MENU_HEIGHT+2, color=(255, 255, 255), batch=batch_bg)
food_fill = py.shapes.Rectangle(food_border.x +1, food_border.y +1, MENU_WIDTH, MENU_HEIGHT, color=(0,0,0), batch=batch_bg)
food_txt = py.text.Label('FOOD', x=food_border.x + food_border.width//2-24, y=food_border.y + food_border.height + 4, bold=True, color=(0,180,20,255), batch=batch_bg)

batch_stats = py.graphics.Batch()
STATS_BUFFER = 60
health_txt = py.text.Label('Thlay', x=stats_fill.x + 11, y=stats_fill.y + 52, batch=batch_stats)
stomach_txt = py.text.Label('Flay', x=stats_fill.x + 20, y=stats_fill.y + 32, batch=batch_stats)
poops_txt = py.text.Label('Hraka', x=stats_fill.x + 8, y=stats_fill.y + 12, batch=batch_stats)
health_val = py.text.Label(thlay.get_stats(), x= stats_fill.x + STATS_BUFFER, y=health_txt.y, batch=batch_stats)
stomach_val = py.text.Label(flay.get_stats(), x= stats_fill.x + STATS_BUFFER, y=stomach_txt.y, batch=batch_stats)
poops_val = py.text.Label(hraka.get_stats(), x = stats_fill.x + STATS_BUFFER, y=poops_txt.y, batch=batch_stats)
food1_txt = py.text.Label('', x= food_fill.x +6, y=food_fill.y + 52, batch=batch_stats)
food2_txt = py.text.Label('', x= food_fill.x +6, y=food_fill.y + 32, batch=batch_stats)
food3_txt = py.text.Label('', x= food_fill.x +6, y=food_fill.y + 12, batch=batch_stats)

batch_tiles = py.graphics.Batch()
coord_tile_top = 430 + 60
#coord_tile_left = 0 + 110 //normal width
coord_tile_left = 0 + 56
coord_tile_dim_y = 84
coord_tile_dim_x = 105

tiles = []
# for row in world_slice:
#     for tile in row:
#         tile = tile.tile.name
#         #food = len(tile.tile.non_colliding_objects) > 0
#         print (f't: {tile} ')
for y in range(5):
    tile_y = coord_tile_top - (y*coord_tile_dim_y)
    for x in range(5):
        tile_y -= coord_tile_dim_y//2
        tile_x = coord_tile_left + (x*coord_tile_dim_x)
        tile = world_slice[y][x].tile.name
        food = len(world_slice[y][x].non_colliding_objects) > 0
        tile_graphic = sprites.Ground()
        tile_graphic.make_tile(tile, tile_x, tile_y)
        tile_graphic.sprite.batch = batch_tiles
        tiles.append(tile_graphic)
        if food == True:
            tile_food = sprites.Grass()
            tile_food.make_tile(tile_x, tile_y)
            tile_food.sprite.batch = batch_tiles
            tiles.append(tile_food)
        print (f't: {tile} f:{food} xy:{tile_x, tile_y}')

# for tile in tiles:
world.render_slice()


@window.event
def on_draw():
    window.clear()
    # bg_color.draw()
    batch_tiles.draw()
    batch_bg.draw()
    batch_stats.draw()
    vair.sprite.draw()
    

@window.event
def on_key_press(symbol, modifiers):
    if not vair.animating:  # ensure no animations are active before receiving input
        if symbol == py.window.key.SPACE:  # skip turn
            on_anim_complete(None)
        elif symbol == py.window.key._1 and len(food1_txt.text) >1:
            world.eat_food(0)
            flay.eat(menu[0])
            vair.nom(on_anim_complete)
            #py.clock.schedule_once(on_anim_complete, 1)
        elif symbol == py.window.key._2 and len(food2_txt.text) >1:
            world.eat_food(1)
            flay.eat(menu[1])
            vair.nom(on_anim_complete)
            #py.clock.schedule_once(on_anim_complete, 1)
        elif symbol == py.window.key._3 and len(food3_txt.text) >1:
            world.eat_food(2)
            flay.eat(menu[2])
            vair.nom(on_anim_complete)
            #py.clock.schedule_once(on_anim_complete, 1)
        elif hraka.poopsAvailable():  # check if we are able to move
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
                    vair.hop_in(hop_side, on_anim_complete)
                else:
                    vair.hop_out(hop_side, on_anim_complete)
                world.move_player(hop_target)
                #py.clock.schedule_once(on_anim_complete, 0.6)

#callback fuction passed into sprites for animation
def on_anim_complete(_):
    #update stomach with number of moves
    flay.update()
    #updates stats
    health_val.text = thlay.get_stats()
    stomach_val.text = flay.get_stats()
    poops_val.text = hraka.get_stats()
    #empty food menu
    food1_txt.text = ''
    food2_txt.text = ''
    food3_txt.text = ''
    #updates food menu
    global menu
    menu = []
    foods_at_loc = world.what_food_is_here()
    print(foods_at_loc)
    for food in foods_at_loc:
        if food not in menu:
            menu.append(food)
    if len(menu) >= 1:
        food1_txt.text = f'#1 : {menu[0].name}'
    if len(menu) >= 2:
        food2_txt.text = f'#2 : {menu[1].name}'
    if len(menu) >= 3:
        food3_txt.text = f'#3 : {menu[2].name}'
    #Check if we died
    if thlay.is_alive() == False:
        pass
        # call end game

    #update graphics to be drawn
    world.render_slice()
    #world_slice = world.return_slice()


if __name__ == '__main__':
    py.app.run()
