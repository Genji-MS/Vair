import pyglet as py
import sprites

py.resource.path = ['../resources']
py.resource.reindex()


def anchor_center(image):
    """set the anchor point of an image to its center"""
    image.anchor_x = image.width//2
    image.anchor_y = image.height//2


vair = sprites.Title_Rabbit()
text = sprites.Title_Text()

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
def on_draw():
    window.clear()
    bg_color.draw()
    vair.sprite.draw()
    text.sprite.draw()


if __name__ == '__main__':
    # creates the event loop
    py.app.run()
