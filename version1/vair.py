import pyglet as py
import sprites
import game.health as Thlay
import game.poops as Hraka
import game.stomach as Flay
import game_map.game_map as World
from pyglet.window import mouse
import random


#////////////////////INIT//////////////////
py.resource.path = ['../resources']
py.resource.reindex()

# Set audio driver priority
py.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
sound_player = py.media.Player()

def anchor_center(image):
    """set the anchor point of an image to its center"""
    image.anchor_x = image.width//2
    image.anchor_y = image.height//2

window = py.window.Window()
bg_color = py.shapes.Rectangle(0, 0, window.width, window.height, color=(22, 78, 22))
seed = 0
world = None #World.GameMap(0)
thlay = Thlay.Health()
hraka = Hraka.Poops()
flay = Flay.Stomach(hraka, thlay)
pos_x, pos_y = None, None
world_slice = None
vair = None
text = None
butn = None
butn2 = None
menu = []
#/////////////GRAPHIC ELEMENTS///////////
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

health_bar = py.shapes.Rectangle(x= stats_fill.x + STATS_BUFFER, y=health_txt.y, height=12, width = thlay.get_bar_update()[0], color=thlay.get_bar_update()[1], batch=batch_bg)
stomach_bar = py.shapes.Rectangle(x= stats_fill.x + STATS_BUFFER, y=stomach_txt.y, height=12, width = flay.get_bar_update()[0], color=flay.get_bar_update()[1], batch=batch_bg)
poop_bar = py.shapes.Rectangle(x= stats_fill.x + STATS_BUFFER, y=poops_txt.y, height=12, width = hraka.get_bar_update()[0], color=hraka.get_bar_update()[1], batch=batch_bg)

health_val = py.text.Label(thlay.get_stats(), x= stats_fill.x + STATS_BUFFER, y=health_txt.y, batch=batch_stats)
stomach_val = py.text.Label(flay.get_stats(), x= stats_fill.x + STATS_BUFFER, y=stomach_txt.y, batch=batch_stats)
poops_val = py.text.Label(hraka.get_stats(),  x= stats_fill.x + STATS_BUFFER, y=poops_txt.y, batch=batch_stats)

food1_txt = py.text.Label('', x= food_fill.x +6, y=food_fill.y + 52, batch=batch_stats)
food2_txt = py.text.Label('', x= food_fill.x +6, y=food_fill.y + 32, batch=batch_stats)
food3_txt = py.text.Label('', x= food_fill.x +6, y=food_fill.y + 12, batch=batch_stats)

batch_tiles = py.graphics.Batch()
tiles = []
batch_objects = py.graphics.Batch()
objects = []
#initialized in init

GAME_MODE = 'intro'

def game_intro():
    global GAME_MODE, sound_player, vair, text, butn, butn2, pos_x, pos_y, world_slice
    GAME_MODE = 'intro'
    #////////////////////INTRO///////////////
    song = py.media.load("../resources/sounds/intro_track.wav", streaming=False)
    sound_player.queue(song)
    #////////////////////////////////////////    
    vair = sprites.Title_Rabbit()
    text = sprites.Title_Text()
    butn = py.resource.image("title/start_button.png")
    butn.width, butn.height = 100, 50
    anchor_center(butn)
    for image in vair.title_seq:
        anchor_center(image)
    for image in text.title_seq:
        anchor_center(image)
    #/////////////UNSCHEDULING///////////////
    clocks = [vair, text]
    for clock in clocks:
        py.clock.unschedule(clock)
    #///////////////SCHEDULING///////////////
    py.clock.schedule_interval(vair.update, 0.07)
    py.clock.schedule_interval(text.update, 0.1)

def game_init(new_map = True):
    global GAME_MODE, sound_player, seed, world, thlay, flay, hraka, vair, text, butn, butn2, pos_x, pos_y, world_slice, batch_bg, batch_stats, batch_tiles, tiles, batch_objects, objects
    GAME_MODE = 'game'
    #/////////////UNSCHEDULING///////////////
    clocks = [vair, text]
    for clock in clocks:
        py.clock.unschedule(clock)
    #////////////////////GAME////////////////
    if new_map:
        seed = random.randint(0,1000000)
    world = World.GameMap(seed)
    pos_x, pos_y = world.player_pos
    world_slice = world.return_slice()
    vair = sprites.Sprite_Rabbit()
    text = None
    butn = None
    butn2 = None
    for image in vair.img_seq:
        anchor_center(image)
    #///////////////////TILES///////////////
    on_anim_complete(0)
    #///////////////SCHEDULING///////////////
    py.clock.schedule_interval(vair.update, 0.07)

def game_outro():
    global GAME_MODE, sound_player, vair, text, butn, butn2, pos_x, pos_y, world_slice
    GAME_MODE = 'outro'
    #//////////////////OUTRO/////////////////
    song = py.media.load("../resources/sounds/game_over.wav", streaming=False)
    sound_player.queue(song)
    #/////////////UNSCHEDULING///////////////
    clocks = [vair, text]
    for clock in clocks:
        py.clock.unschedule(clock)
    #////////////////////////////////////////
    #world_slice keep ?
    vair = sprites.Dead_Rabbit()
    text = None
    butn = py.resource.image("title/NewMap.png")
    butn2 = py.resource.image("title/SameMap.png")
    butn.width, butn.height = 100, 50
    butn2.width, butn2.height = 100, 50
    anchor_center(butn)
    anchor_center(butn2)
    for image in vair.img_seq:
        anchor_center(image)
    #///////////////SCHEDULING///////////////
    py.clock.schedule_interval(vair.update, 0.07)

def on_anim_complete(_):
    global GAME_MODE, sound_player, world, thlay, flay, hraka, vair, text, pos_x, pos_y, world_slice, menu, health_val, stomach_val, poops_val, food1_txt, food2_txt, food3_txt, batch_tiles, tiles, batch_objects, objects
    #update stomach with number of moves
    flay.update()
    #updates stats
    health_val.text = thlay.get_stats()
    health_bar.width = thlay.get_bar_update()[0] 
    health_bar.color = thlay.get_bar_update()[1]
    stomach_val.text = flay.get_stats()
    stomach_bar.width = flay.get_bar_update()[0] 
    stomach_bar.color =  flay.get_bar_update()[1] 
    poops_val.text = hraka.get_stats()
    poop_bar.width = hraka.get_bar_update()[0]
    poop_bar.color = hraka.get_bar_update()[1]
    #empty food menu
    food1_txt.text = ''
    food2_txt.text = ''
    food3_txt.text = ''
    #updates food menu
    menu = []
    foods_at_loc = world.what_food_is_here()
    #print(foods_at_loc)
    for food in foods_at_loc:
        if food.name not in menu:
            menu.append(food)
    if len(menu) >= 1:
        food1_txt.text = f'#1 : {menu[0].name}'
    if len(menu) >= 2:
        food2_txt.text = f'#2 : {menu[1].name}'
    if len(menu) >= 3:
        food3_txt.text = f'#3 : {menu[2].name}'
   
    #world.render_slice()  #draws map to terminal
    #tile defaults
    world_slice = world.return_slice()
    coord_tile_top = 430 + 60
    coord_tile_left = 0 + 56
    coord_tile_dim_y = 84
    coord_tile_dim_x = 105
    #update graphics to be drawn
    tiles = []
    objects = []
    for y in range(5):
        tile_y = coord_tile_top - (y*coord_tile_dim_y)
        for x in range(5):
            tile_y -= coord_tile_dim_y//2
            tile_x = coord_tile_left + (x*coord_tile_dim_x)
            #create floor tiles
            tile = world_slice[y][x].tile.name
            tile_graphic = sprites.Ground()
            tile_graphic.make_tile(tile, tile_x, tile_y)
            tile_graphic.sprite.batch = batch_tiles
            tiles.append(tile_graphic)
            #create food tiles
            foods = world_slice[y][x].non_colliding_objects
            if len(foods) > 0:
                food_list = []
                for food in foods:
                    if food.name not in food_list:
                        food_list.append(food.name)
                #print (f'foods {food_list}')
                if 'allthesame' in food_list:
                    tile_food = sprites.Grass()
                    tile_food.make_tile(tile_x, tile_y)
                    tile_food.sprite.batch = batch_objects
                    objects.append(tile_food)
                if 'Poop' in food_list:
                    tile_poop = sprites.Poop()
                    tile_poop.make_tile(tile_x, tile_y)
                    tile_poop.sprite.batch = batch_objects
                    objects.append(tile_poop)
            # check for rock
            rocks = world_slice[y][x].colliding_objects
            if len(rocks) > 0:
                for rock in rocks:
                    #rocks are of ascii value '\x1b[37mR' rabbit is '\x1b[31mX' parse for 'R'
                    if rock[-1] == 'R':
                        tile_rock = sprites.Rock()
                        tile_rock.make_tile(tile_x, tile_y)
                        tile_rock.sprite.batch = batch_objects
                        objects.append(tile_rock)
                        #print (f'rock: {rock}')
    #Check if we died
    if thlay.is_alive() == False:
        game_outro()
    #world_slice = world.return_slice()

game_intro()
#////////////////////////////////////////
@window.event
def on_mouse_press(x, y, button, modifiers):
    global GAME_MODE
    if button == mouse.LEFT:
        if GAME_MODE == 'intro':
            #Intro
            if x > 275 and x < 375:
                if y > 25 and y < 75:
                    #print("you clicked the start button")
                    thlay.new_game()
                    hraka.new_game()
                    flay.new_game()
                    game_init(True)
                    # insert game transition here
                    # discard player() object playing the song here
        if GAME_MODE == 'outro':
            #Outro
            if x > 175 and x < 275:
                if y > 25 and y < 75:
                    #print("New Map")
                    thlay.new_game()
                    hraka.new_game()
                    flay.new_game()
                    game_init(True)
            elif x > 375 and x < 475:
                if y > 25 and y < 75:
                    #print("Same Map")
                    thlay.new_game()
                    hraka.new_game()
                    flay.new_game()
                    game_init(False)
                # insert game transition here
                # discard player() object playing the song here

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

@window.event
def on_draw():
    global GAME_MODE
    if GAME_MODE == 'intro':
        #///////INTRO///////
        window.clear()
        bg_color.draw()
        vair.sprite.draw()
        text.sprite.draw()
        butn.blit(325, 55)
        sound_player.play()
    elif GAME_MODE == 'outro':
        #//////OUTRO////////
        window.clear()
        bg_color.draw()
        vair.sprite.draw()
        butn.blit(225, 55)
        butn2.blit(425, 55)
        sound_player.play()
    elif GAME_MODE == 'game':
        #//////GAME////////
        window.clear()
        # bg_color.draw()
        batch_tiles.draw()
        batch_objects.draw()
        batch_bg.draw()
        batch_stats.draw()
        vair.sprite.draw()

#////////////////////////////////////////

if __name__ == '__main__':
    # creates the event loop
    py.app.run()