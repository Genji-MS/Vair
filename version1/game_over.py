import pyglet as py
from pyglet.window import mouse
import sprites

py.resource.path = ['../resources']
py.resource.reindex()


# Set audio driver priority
py.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
#replace intro with death song
game_over = py.media.load("./resources/sounds/intro_track.wav", streaming=False)
sound_player = py.media.Player()
sound_player.queue(game_over)


def anchor_center(image):
    """set the anchor point of an image to its center"""
    image.anchor_x = image.width//2
    image.anchor_y = image.height//2


vair = sprites.Title_Rabbit()
text = sprites.Title_Text()
# giving start button an anchor
new_map = py.resource.image("title/NewMap.png")
same_map = py.resource.image("title/SameMap.png")
new_map.width, new_map.height = 100, 50
same_map.width, same_map.height = 100, 50
anchor_center(new_map)
anchor_center(same_map)

for image in vair.title_seq:
    anchor_center(image)
for image in text.title_seq:
    anchor_center(image)

window = py.window.Window()
bg_color = py.shapes.Rectangle(
    0, 0, window.width, window.height, color=(22, 78, 22))

py.clock.schedule_interval(vair.update, 0.1)
py.clock.schedule_interval(text.update, 0.1)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        if x > 175 and x < 275:
            if y > 25 and y < 75:
                print("New Map")
        elif x > 375 and x < 475:
            if y > 25 and y < 75:
                print("Same Map")
                # insert game transition here
                # discard player() object playing the song here


@window.event
def on_draw():
    window.clear()
    bg_color.draw()
    vair.sprite.draw()
    text.sprite.draw()
    new_map.blit(225, 55)
    same_map.blit(425, 55)
    sound_player.play()


if __name__ == '__main__':
    # creates the event loop
    py.app.run()
