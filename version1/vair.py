import pyglet as py
import sprites
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
vair = None
text = None
butn = None
butn2 = None
GAME_MODE = 'intro'

def game_intro():
    global GAME_MODE, sound_player, vair, text, butn, butn2
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
    # SCHEDULE intro 
    py.clock.schedule_interval(vair.update, 0.07)
    py.clock.schedule_interval(text.update, 0.1)

def game_outro():
    global GAME_MODE, sound_player, vair, text, butn, butn2
    GAME_MODE = 'outro'
    #//////////////////OUTRO/////////////////
    song = py.media.load("../resources/sounds/game_over.wav", streaming=False)
    sound_player.queue(song)

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
    #/////////////UNSCHEDULING///////////////
    clocks = [vair, text]
    for clock in clocks:
        py.clock.unschedule(clock)
    # SCHEDULE outro
    py.clock.schedule_interval(vair.update, 0.07)

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
                    game_outro()
                    # insert game transition here
                    # discard player() object playing the song here
        if GAME_MODE == 'outro':
            #Outro
            if x > 175 and x < 275:
                if y > 25 and y < 75:
                    print("New Map")
                    game_intro()
            elif x > 375 and x < 475:
                if y > 25 and y < 75:
                    print("Same Map")
                # insert game transition here
                # discard player() object playing the song here

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

#////////////////////////////////////////

if __name__ == '__main__':
    # creates the event loop
    py.app.run()

