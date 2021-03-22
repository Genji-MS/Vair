import pyglet as py
import sprites
import game.health as Thlay
import game.poops as Hraka
import game.stomach as Flay
import game_map.game_map as World
from pyglet.window import mouse


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
world = World.GameMap(0)
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
batch_bg = py.graphics.Batch()
batch_stats = py.graphics.Batch()
#/////////////GRAPHIC ELEMENTS///////////
BUFFER = 8  # padding
STATS_BUFFER = 60
stats_border = py.shapes.Rectangle((BUFFER//2)-1, window.height - (75+1) - (BUFFER//2), 120+2, 74+2, color=(255, 255, 255), batch=batch_bg)
stats_fill = py.shapes.Rectangle(BUFFER//2, window.height - 75 - (BUFFER//2), 120, 74, color=(0, 0, 0), batch=batch_bg)
food_border = py.shapes.Rectangle(window.width - stats_border.x - stats_border.width, stats_border.y, stats_border.width, stats_border.height, color=(255, 255, 255), batch=batch_bg)
food_fill = py.shapes.Rectangle(window.width - stats_fill.x - stats_fill.width, stats_fill.y, stats_fill.width, stats_fill.height, color=(0,0,0), batch=batch_bg)
health_txt = py.text.Label('Thlay', x=BUFFER + 3, y=window.height - 20 - BUFFER, batch=batch_stats)
stomach_txt = py.text.Label('Flay', x=BUFFER + 12, y=window.height - 40 - BUFFER, batch=batch_stats)
poops_txt = py.text.Label('Hraka', x=BUFFER, y=window.height - 60 - BUFFER, batch=batch_stats)
health_bar = py.shapes.Rectangle(x=STATS_BUFFER, y=health_txt.y, width=thlay.get_bar_update()[0], height=12, color=thlay.get_bar_update()[1], batch=batch_stats)
stomach_bar = py.shapes.Rectangle(x=STATS_BUFFER, y=stomach_txt.y, width=flay.get_bar_update()[0], height=12, color=flay.get_bar_update()[1], batch=batch_stats)
poop_bar = py.shapes.Rectangle(x=STATS_BUFFER, y=poops_txt.y, width=hraka.get_bar_update()[0], height=12, color=hraka.get_bar_update()[1], batch=batch_stats)
health_val = py.text.Label(thlay.get_stats(), x= STATS_BUFFER, y=health_txt.y, batch=batch_stats)
stomach_val = py.text.Label(flay.get_stats(), x= STATS_BUFFER, y=stomach_txt.y, batch=batch_stats)
poops_val = py.text.Label(hraka.get_stats(), x = STATS_BUFFER, y=poops_txt.y, batch=batch_stats)
food1_txt = py.text.Label('', x= food_fill.x +6, y = health_txt.y, batch=batch_stats)
food2_txt = py.text.Label('', x= food_fill.x +6, y=stomach_txt.y, batch=batch_stats)
food3_txt = py.text.Label('', x= food_fill.x +6, y=poops_txt.y, batch=batch_stats)
stats_txt = py.text.Label('STATS', x=stats_border.x + stats_border.width//2-30, y=window.height-13, bold=True, color=(0,180,20,255), batch=batch_stats)
food_txt = py.text.Label('FOOD', x=food_border.x + stats_border.width//2-20, y=window.height-13, bold=True, color=(0,180,20,255), batch=batch_stats)

GAME_MODE = 'intro'

def game_intro():
    global GAME_MODE, sound_player, vair, text, butn, butn2, pos_x, pos_y, world_slice
    GAME_MODE = 'intro'
    #////////////////////INTRO///////////////
    song = py.media.load("./resources/sounds/intro_track.wav", streaming=False)
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
    # SCHEDULE intro 
    py.clock.schedule_interval(vair.update, 0.07)
    py.clock.schedule_interval(text.update, 0.1)

def game_init(new_or_same_map = 'new'):
    global GAME_MODE, sound_player, world, thlay, flay, hraka, vair, text, butn, butn2, pos_x, pos_y, world_slice, batch_bg, batch_stats
    GAME_MODE = 'game'
    #/////////////UNSCHEDULING///////////////
    clocks = [vair, text]
    for clock in clocks:
        py.clock.unschedule(clock)
    #////////////////////GAME////////////////
    pos_x, pos_y = world.player_pos
    world_slice = world.return_slice()
    vair = sprites.Sprite_Rabbit()
    text = None
    butn = None
    butn2 = None
    for image in vair.img_seq:
        anchor_center(image)
    # SCHEDULE game
    py.clock.schedule_interval(vair.update, 0.07)

def game_outro():
    global GAME_MODE, sound_player, vair, text, butn, butn2, pos_x, pos_y, world_slice
    GAME_MODE = 'outro'
    #//////////////////OUTRO/////////////////
    song = py.media.load("./resources/sounds/game_over.wav", streaming=False)
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
    # SCHEDULE outro
    py.clock.schedule_interval(vair.update, 0.07)

def on_anim_complete(_):
    global GAME_MODE, sound_player, world, thlay, flay, hraka, vair, text, pos_x, pos_y, world_slice, menu, health_bar, stomach_bar, poop_bar, health_val, stomach_val, poops_val, food1_txt, food2_txt, food3_txt
    #update stomach with number of moves
    flay.update()
    #updates stats
    health_val.text = thlay.get_stats()
    health_bar.width = thlay.get_bar_update()[0] #ADDED THIS LINE
    health_bar.color = thlay.get_bar_update()[1]
    stomach_val.text = flay.get_stats()
    stomach_bar.width = flay.get_bar_update()[0] #added this line
    stomach_bar.color =  flay.get_bar_update()[1] #added this line
    poops_val.text = hraka.get_stats()
    poop_bar.width = hraka.get_bar_update()[0] #added this line
    poop_bar.color = hraka.get_bar_update()[1] #added this line
    #empty food menu
    food1_txt.text = ''
    food2_txt.text = ''
    food3_txt.text = ''
    #updates food menu
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
        game_outro()
        # call end game

    #update graphics to be drawn
    world.render_slice()
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
                    print("you clicked the start button")
                    game_init()
                    # insert game transition here
                    # discard player() object playing the song here
        if GAME_MODE == 'outro':
            #Outro
            if x > 175 and x < 275:
                if y > 25 and y < 75:
                    print("New Map")
                    game_init()
            elif x > 375 and x < 475:
                if y > 25 and y < 75:
                    print("Same Map")
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
        # DRAW TILES
        batch_bg.draw()
        batch_stats.draw()
        vair.sprite.draw()

#////////////////////////////////////////

if __name__ == '__main__':
    # creates the event loop
    py.app.run()