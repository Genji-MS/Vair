import pyglet as py
#from game import resources

#set image path and specific sprites to files
py.resource.path = ['../resources']
py.resource.reindex()
p_img = py.resource.image("bun_idle_0-90-cmb.png")
e_img = py.resource.image("fox_1.png")
g_0 = py.resource.image("g_brn_1.png")
g_1 = py.resource.image("g_yelo_1.png")
g_2 = py.resource.image("g_wht_2.png")
g_3 = py.resource.image("g_green_6.png")
g_4 = py.resource.image("g_d_grn_2.png")

def anchor_center(image):
    """set the anchor point of an image to its center"""
    image.anchor_x = image.width//2
    image.anchor_y = image.height//2

images = [p_img, e_img, g_0, g_1, g_2, g_3, g_4]
for image in images:
    anchor_center(image)

#create game window
window = py.window.Window()
#create a text label
#label = py.text.Label('Vair', x=window.width//2, y=window.height//2)
health_txt = py.text.Label('Thlay', y=window.height - 10)
stomach_txt = py.text.Label('Flay', y=window.height - 20)
poops_txt = py.text.Label('Hraka', y=window.height - 30)

player = py.sprite.Sprite(img=resources.p_img, x=100, y=50)
enemy = py.sprite.Sprite(img=resources.e_img, x=250, y=200)



#event handeler
@window.event
def on_draw():
    window.clear()
    player.draw()
    enemy.draw()
    health_txt.draw()
    stomach_txt.draw()
    poops_txt.draw()

if __name__ == '__main__':
#creates the event loop
    py.app.run()