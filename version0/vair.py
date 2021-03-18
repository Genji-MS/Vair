import pyglet as py
import sprites

#set image path and specific sprites to files
py.resource.path = ['../resources']
py.resource.reindex()

def anchor_center(image):
    """set the anchor point of an image to its center"""
    image.anchor_x = image.width//2
    image.anchor_y = image.height//2

#instantiate the title rabbit animation class
vair = sprites.Title_Rabbit()
bun = sprites.Sprite_Rabbit()
fox = sprites.Sprite_Fox()
text = sprites.Title_Text()
#re-center images
for image in vair.title_seq:
    anchor_center(image)
for image in bun.img_seq:
    anchor_center(image)
for image in fox.img_seq:
    anchor_center(image)
for image in text.title_seq:
    anchor_center(image)

#create game window
window = py.window.Window()
batch = py.graphics.Batch()
bg_color = py.shapes.Rectangle(0,0,window.width, window.height, color=(22, 78, 22))


#create some text labels
BUFFER = 8 #padding
stats_border = py.shapes.Rectangle((BUFFER//2)-1, window.height - (75+1) - (BUFFER//2), 120+2, 74+2, color = (255,255,255), batch = batch)
stats_fill = py.shapes.Rectangle(BUFFER//2, window.height - 75 - (BUFFER//2), 120, 74, color = (0,0,0), batch = batch)
health_txt = py.text.Label('Thlay', x= BUFFER, y=window.height - 20 -BUFFER, batch = batch)
stomach_txt = py.text.Label('Flay', x= BUFFER, y=window.height - 40 -BUFFER, batch = batch)
poops_txt = py.text.Label('Hraka', x= BUFFER, y=window.height - 60 -BUFFER, batch = batch)
#title_txt = py.text.Label('air', font_size = 78, x = vair.sprite.x + 10, y=vair.sprite.y + 40)

#calls our animation instance to update every 0.1 seconds
py.clock.schedule_interval(vair.update, 0.1)
py.clock.schedule_interval(bun.update, 0.07)
py.clock.schedule_interval(fox.update, 0.1)
py.clock.schedule_interval(text.update, 0.1)

#event handeler
@window.event
def on_draw():
    window.clear()
    bg_color.draw()
    vair.sprite.draw()
    bun.sprite.draw()
    fox.sprite.draw()
    batch.draw()
    text.sprite.draw()
    #title_txt.draw()

#forces a redraw, will create flicker if used excessivly
#window.flip()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == py.window.key.SPACE:
        bun.nom()
    elif symbol == py.window.key.Q:
        bun.hop_out('L')
        # bun.x += 10
        # bun.y += 10
    elif symbol == py.window.key.A:
        bun.hop_in('L')
    elif symbol == py.window.key.E:
        bun.hop_out('R')
    elif symbol == py.window.key.D:
        bun.hop_in('R')
    elif symbol == py.window.key.W:
        bun.hop_out()
    elif symbol == py.window.key.S:
        bun.hop_in()


if __name__ == '__main__':
    #creates the event loop
    py.app.run()