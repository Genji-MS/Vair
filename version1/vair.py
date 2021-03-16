import pyglet as py

class Sprite_Rabbit:
    def __init__(self):
        self.frame = 0
        self.frameMAX = 8
        self.title0 = py.resource.image("bun_idle_0-title.png")
        self.title1 = py.resource.image("bun_idle_1-title.png")
        self.title2 = py.resource.image("bun_idle_2-title.png")
        self.title3 = py.resource.image("bun_idle_3-title.png")
        self.title4 = py.resource.image("bun_idle_4-title.png")
        self.title5 = py.resource.image("bun_idle_5-title.png")
        self.title6 = py.resource.image("bun_idle_6-title.png")
        self.title7 = py.resource.image("bun_idle_7-title.png")
        self.title_seq = [self.title0, self.title1, self.title2, 
                        self.title3, self.title4, self.title5,
                        self.title6, self.title7]
        self.update(0)
    def update(self, _):
        #clock sends a parameter. '_' used (as in GO) to denote a variable we don't use
        self.frame += 1 #increments the array to use the next image %(mod) the length of the array
        self.sprite = py.sprite.Sprite(img = self.title_seq[self.frame%self.frameMAX], x=280, y=250)
    

#set image path and specific sprites to files
py.resource.path = ['../resources']
py.resource.reindex()

def anchor_center(image):
    """set the anchor point of an image to its center"""
    image.anchor_x = image.width//2
    image.anchor_y = image.height//2

#instantiate the title rabbit animation class
vair = Sprite_Rabbit()
#re-center images
for image in vair.title_seq:
    anchor_center(image)

#create game window
window = py.window.Window()
batch = py.graphics.Batch()
bg_color = py.shapes.Rectangle(0,0,window.width, window.height, color=(79, 78, 66))


#create some text labels
BUFFER = 8 #padding
stats_border = py.shapes.Rectangle((BUFFER//2)-1, window.height - (75+1) - (BUFFER//2), 120+2, 74+2, color = (255,255,255), batch = batch)
stats_fill = py.shapes.Rectangle(BUFFER//2, window.height - 75 - (BUFFER//2), 120, 74, color = (0,0,0), batch = batch)
health_txt = py.text.Label('Thlay', x= BUFFER, y=window.height - 20 -BUFFER, batch = batch)
stomach_txt = py.text.Label('Flay', x= BUFFER, y=window.height - 40 -BUFFER, batch = batch)
poops_txt = py.text.Label('Hraka', x= BUFFER, y=window.height - 60 -BUFFER, batch = batch)
title_txt = py.text.Label('air', font_size = 78, x = vair.sprite.x + 10, y=vair.sprite.y + 40)

#calls our animation instance to update every 0.1 seconds
py.clock.schedule_interval(vair.update, 0.1)

#event handeler
@window.event
def on_draw():
    window.clear()
    bg_color.draw()
    vair.sprite.draw()
    batch.draw()
    title_txt.draw()

if __name__ == '__main__':
    #creates the event loop
    py.app.run()