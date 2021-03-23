import pyglet as py
import random

py.resource.path = ['../resources']
py.resource.reindex()

class Title_Rabbit:
    def __init__(self):
        self.frame = 0
        self.frameMAX = 8
        self.animating = True
        self.title0 = py.resource.image("title/bun_60_2_0.png")
        self.title1 = py.resource.image("title/bun_60_2_1.png")
        self.title2 = py.resource.image("title/bun_60_2_2.png")
        self.title3 = py.resource.image("title/bun_60_2_3.png")
        self.title4 = py.resource.image("title/bun_60_2_4.png")
        self.title5 = py.resource.image("title/bun_60_2_5.png")
        self.title6 = py.resource.image("title/bun_60_2_6.png")
        self.title7 = py.resource.image("title/bun_60_2_7.png")
        self.title_seq = [self.title0, self.title1, self.title2, 
                        self.title3, self.title4, self.title5,
                        self.title6, self.title7]
        self.update(0)
    def update(self, _):
        #clock sends a parameter. '_' used (as in GO) to denote a variable we don't use
        self.frame += 1 #increments the array to use the next image %(mod) the length of the array
        self.sprite = py.sprite.Sprite(img = self.title_seq[self.frame%self.frameMAX], x=280, y=250)

class Title_Text:
    def __init__(self):
        self.frame = 0
        self.frameMAX = 8
        self.title0 = py.resource.image("title/txt_0002_air_0.png")
        self.title1 = py.resource.image("title/txt_0002_air_1.png")
        self.title2 = py.resource.image("title/txt_0002_air_2.png")
        self.title3 = py.resource.image("title/txt_0002_air_3.png")
        self.title4 = py.resource.image("title/txt_0002_air_4.png")
        self.title5 = py.resource.image("title/txt_0002_air_5.png")
        self.title6 = py.resource.image("title/txt_0002_air_6.png")
        self.title7 = py.resource.image("title/txt_0002_air_7.png")
        self.title_seq = [self.title0, self.title1, self.title2, 
                        self.title3, self.title4, self.title5,
                        self.title6, self.title7]
        self.update(0)
    def update(self, _):
        #clock sends a parameter. '_' used (as in GO) to denote a variable we don't use
        self.frame += 1 #increments the array to use the next image %(mod) the length of the array
        self.sprite = py.sprite.Sprite(img = self.title_seq[self.frame%self.frameMAX], x = 367, y=320)
        self.sprite.scale = 1.3

class Title_Text_Alt:
    def __init__(self):
        self.frame = 0
        self.frameMAX = 8
        self.title0 = py.resource.image("title/txt_0015_air_0.png")
        self.title1 = py.resource.image("title/txt_0015_air_1.png")
        self.title2 = py.resource.image("title/txt_0015_air_2.png")
        self.title3 = py.resource.image("title/txt_0015_air_3.png")
        self.title4 = py.resource.image("title/txt_0015_air_4.png")
        self.title5 = py.resource.image("title/txt_0015_air_5.png")
        self.title6 = py.resource.image("title/txt_0015_air_6.png")
        self.title7 = py.resource.image("title/txt_0015_air_7.png")
        self.title_seq = [self.title0, self.title1, self.title2, 
                        self.title3, self.title4, self.title5,
                        self.title6, self.title7]
        self.update(0)
    def update(self, _):
        #clock sends a parameter. '_' used (as in GO) to denote a variable we don't use
        self.frame += 1 #increments the array to use the next image %(mod) the length of the array
        self.sprite = py.sprite.Sprite(img = self.title_seq[self.frame%self.frameMAX], x = 365, y=313)

class Dead_Rabbit:
    def __init__(self):
        self.frame = 0
        self.frameMAX = 8
        self.animating = True
        self.scale_x = 1
        self.x = 325
        self.y = 250
        self.ded0 = py.resource.image("rabbit/bun_ded_0.png")
        self.ded1 = py.resource.image("rabbit/bun_ded_1.png")
        self.ded2 = py.resource.image("rabbit/bun_ded_2.png")
        self.ded3 = py.resource.image("rabbit/bun_ded_3.png")
        self.ded4 = py.resource.image("rabbit/bun_ded_4.png")
        self.ded5 = py.resource.image("rabbit/bun_ded_5.png")
        self.ded6 = py.resource.image("rabbit/bun_ded_6.png")
        self.ded7 = py.resource.image("rabbit/bun_ded_7.png")
        self.img_seq = [self.ded0, self.ded1, self.ded2,
                        self.ded3, self.ded4, self.ded5,
                        self.ded6, self.ded7]
        self.update(0)
    def update(self, _):
        #clock sends a parameter. '_' used (as in GO) to denote a variable we don't use
        self.frame += 1 #increments the array to use the next image %(mod) the length of the array
        #get next image and update our sprite refference
        currentFrame = self.frame%self.frameMAX
        self.sprite = py.sprite.Sprite(img = self.img_seq[currentFrame], x= self.x, y = self.y)

        self.sprite.scale_x = self.scale_x

class Sprite_Rabbit:
    def __init__(self):
        self.frame = 0
        self.frameMAX = 8
        self.x = 320
        self.y = 280
        self.scale_x = 1
        self.animating = False
        self._callback = None
        self.img0 = py.resource.image("rabbit/bun_idle_0.png")
        self.img1 = py.resource.image("rabbit/bun_idle_1.png")
        self.img2 = py.resource.image("rabbit/bun_idle_2.png")
        self.img3 = py.resource.image("rabbit/bun_idle_3.png")
        self.img4 = py.resource.image("rabbit/bun_idle_4.png")
        self.img5 = py.resource.image("rabbit/bun_idle_5.png")
        self.img6 = py.resource.image("rabbit/bun_idle_6.png")
        self.img7 = py.resource.image("rabbit/bun_idle_7.png")
        self.hopA0 = py.resource.image("rabbit/bun_hop1_2.png")
        self.hopA1 = py.resource.image("rabbit/bun_hop1_1.png")
        self.hopA2 = py.resource.image("rabbit/bun_hop1_5.png")
        self.hopA3 = py.resource.image("rabbit/bun_hop2_6.png")
        self.hopA4 = py.resource.image("rabbit/bun_hop2_4.png")
        self.hopA5 = py.resource.image("rabbit/bun_hop2_5.png")
        self.hopA6 = py.resource.image("rabbit/bun_hop2_1.png")
        self.hopA7 = py.resource.image("rabbit/bun_hop2_0.png")
        self.hopB0 = py.resource.image("rabbit/bun_hopB1_5.png")
        self.hopB1 = py.resource.image("rabbit/bun_hopB1_3.png")
        self.hopB2 = py.resource.image("rabbit/bun_hopB1_7.png")
        self.hopB3 = py.resource.image("rabbit/bun_hopB2_7.png")
        self.hopB4 = py.resource.image("rabbit/bun_hopB2_5.png")
        self.hopB5 = py.resource.image("rabbit/bun_hopB2_6.png")
        self.hopB6 = py.resource.image("rabbit/bun_hopB2_0.png")
        self.hopB7 = py.resource.image("rabbit/bun_hopB2_4.png")
        self.nom0 = py.resource.image("rabbit/bun_nom3_0.png")
        self.nom1 = py.resource.image("rabbit/bun_nom3_1.png")
        self.nom2 = py.resource.image("rabbit/bun_nom3_2.png")
        self.nom3 = py.resource.image("rabbit/bun_nom3_3.png")
        self.nom4 = py.resource.image("rabbit/bun_nom3_4.png")
        self.nom5 = py.resource.image("rabbit/bun_nom3_5.png")
        self.nom6 = py.resource.image("rabbit/bun_nom3_6.png")
        self.nom7 = py.resource.image("rabbit/bun_nom3_7.png")
        self.ded0 = py.resource.image("rabbit/bun_ded_0.png")
        self.ded1 = py.resource.image("rabbit/bun_ded_1.png")
        self.ded2 = py.resource.image("rabbit/bun_ded_2.png")
        self.ded3 = py.resource.image("rabbit/bun_ded_3.png")
        self.ded4 = py.resource.image("rabbit/bun_ded_4.png")
        self.ded5 = py.resource.image("rabbit/bun_ded_5.png")
        self.ded6 = py.resource.image("rabbit/bun_ded_6.png")
        self.ded7 = py.resource.image("rabbit/bun_ded_7.png")
        self.img_seq = [self.img0, self.img1, self.img2, self.img3, 
                        self.img4, self.img5, self.img6, self.img7, 
                        self.hopA0, self.hopA1, self.hopA2, self.hopA3, 
                        self.hopA4, self.hopA5, self.hopA6, self.hopA7,
                        self.hopB0, self.hopB1, self.hopB2, self.hopB3,
                        self.hopB4, self.hopB5, self.hopB6, self.hopB7,
                        self.nom0, self.nom1, self.nom2, self.nom3,
                        self.nom4, self.nom5, self.nom6, self.nom7,
                        self.nom0, self.nom1, self.nom2, self.nom3,
                        self.nom4, self.nom5]
        self.update(0)
    def update(self, _):
        #clock sends a parameter. '_' used (as in GO) to denote a variable we don't use
        if self.frameMAX == 8:
            self.frame = random.randint(0,7)
        else: self.frame += 1 #increments the array to use the next image %(mod) the length of the array
        if self.frame == self.frameMAX == 16 or self.frame == self.frameMAX == 24:
            #resets our jumping frame cycle back to idle animation
            self.end_animation()
        elif self.frame == self.frameMAX == 38:
            #resets our eating cycle to idle
            self.end_animation()
            #fix the eat from being reversed
            if self.scale_x > 0:
                self.scale_x = -1
            else:
                self.scale_x = 1

        #get next image and update our sprite refference
        currentFrame = self.frame%self.frameMAX
        self.sprite = py.sprite.Sprite(img = self.img_seq[currentFrame], x= self.x, y = self.y)

        self.sprite.scale_x = self.scale_x
        if currentFrame < 8:
            self.sprite.scale = 0.6
        elif 7 < currentFrame < 11:
            self.sprite.y -= 15
            self.sprite.scale = 0.45
        elif 10 < currentFrame < 16:
            #makes the sprite rise over time in a glide
            self.sprite.y -= 15
            self.sprite.y += (currentFrame/10) * 10
            self.sprite.scale = 0.5
        elif 15 < currentFrame < 19:
            self.sprite.y -= 25
            self.sprite.scale = 0.5
        elif 18 < currentFrame < 24:
            #makes the sprite fall over time in a glide
            self.sprite.y -= 30 + (currentFrame/10) * 10
            self.sprite.scale = 0.7
        else: 
            self.sprite.scale = 0.44
            #makes the sprite bounce (eating)
            self.sprite.scale_y = 1.1-(currentFrame%5)/30
            self.sprite.y -= 27
    def hop_out(self, ro, _cb):
        if self.frameMAX == 8:
            if ro == 'L':
                self.scale_x = -1
            elif ro == 'R':
                self.scale_x = 1
            self.frame = 8
            self.frameMAX = 16
            self.animating = True
            self._callback = _cb
    def hop_in(self, ro, _cb):
        if self.frameMAX == 8:
            if ro == 'L':
                self.scale_x = -1
            elif ro == 'R':
                self.scale_x = 1
            self.frame = 16
            self.frameMAX = 24
            self.animating = True
            self._callback = _cb
    def nom(self, _cb):
        if self.frameMAX == 8:
            if self.scale_x > 0:
                self.scale_x = -1
            else:
                self.scale_x = 1
            self.frame = 24
            self.frameMAX = 38
            self.animating = True
            self._callback = _cb
    def end_animation(self):
        self.animating = False
        self.frameMAX = 8
        if self._callback:
            self._callback(None)

class Sprite_Fox:
    def __init__(self):
        self.frame = 0
        self.frameMAX = 8
        self.img0 = py.resource.image("fox/fox_x_0.png")
        self.img1 = py.resource.image("fox/fox_x_1.png")
        self.img2 = py.resource.image("fox/fox_x_2.png")
        self.img3 = py.resource.image("fox/fox_x_3.png")
        self.img4 = py.resource.image("fox/fox_x_4.png")
        self.img5 = py.resource.image("fox/fox_x_5.png")
        self.img6 = py.resource.image("fox/fox_x_6.png")
        self.img7 = py.resource.image("fox/fox_x_7.png")
        self.img_seq = [self.img0, self.img1, self.img2, self.img3, 
                        self.img4, self.img5, self.img6, self.img7]
        self.update(0)
        
    def update(self, _):
        #clock sends a parameter. '_' used (as in GO) to denote a variable we don't use
        self.frame += 1 #increments the array to use the next image %(mod) the length of the array
        currentFrame = self.frame%self.frameMAX
        self.sprite = py.sprite.Sprite(img = self.img_seq[currentFrame], x=420, y=140) 
        self.sprite.scale = 0.6

class Water:
    def __init__(self):
        self.ocean0 = py.resource.image("tiles_bezier/g_blue_0.png")
        self.ocean1 = py.resource.image("tiles_bezier/g_blue_1.png")
        self.ocean2 = py.resource.image("tiles_bezier/g_blue_2.png")
        self.ocean3 = py.resource.image("tiles_bezier/g_blue_3.png")
        self.ocean4 = py.resource.image("tiles_bezier/g_blue_4.png")
        self.ocean5 = py.resource.image("tiles_bezier/g_blue_5.png")
        self.ocean6 = py.resource.image("tiles_bezier/g_blue_6.png")
        self.ocean7 = py.resource.image("tiles_bezier/g_blue_7.png")
        self.ocean_seq = [self.ocean0, self.ocean1, self.ocean2,
                            self.ocean3, self.ocean4, self.ocean5,
                            self.ocean6, self.ocean7]
    def make_tile(self, tile_type,x=0,y=0,frame=-1):
        self.make_ocean(x,y,frame)
        self.sprite.scale = 1
        self.sprite.scale_x = 1.25
    def make_ocean(self, x=0, y=0, frame = -1):
        if frame == -1:
            frame = random.randint(0,7)
        self.sprite = py.sprite.Sprite(img = self.ocean_seq[frame], x= x, y = y)

class Ground:
    def __init__(self):
        self.frame = 0
        self.prairie0 = py.resource.image("tiles/g_green_0.png")
        self.prairie1 = py.resource.image("tiles/g_green_1.png")
        self.prairie2 = py.resource.image("tiles/g_green_2.png")
        self.prairie3 = py.resource.image("tiles/g_green_3.png")
        self.prairie4 = py.resource.image("tiles/g_green_4.png")
        self.prairie5 = py.resource.image("tiles/g_green_5.png")
        self.prairie6 = py.resource.image("tiles/g_green_6.png")
        self.prairie7 = py.resource.image("tiles/g_green_7.png")
        self.lush0 = py.resource.image("tiles/g_d_grn_0.png")
        self.lush1 = py.resource.image("tiles/g_d_grn_1.png")
        self.lush2 = py.resource.image("tiles/g_d_grn_2.png")
        self.lush3 = py.resource.image("tiles/g_d_grn_3.png")
        self.lush4 = py.resource.image("tiles/g_d_grn_4.png")
        self.lush5 = py.resource.image("tiles/g_d_grn_5.png")
        self.lush6 = py.resource.image("tiles/g_d_grn_6.png")
        self.lush7 = py.resource.image("tiles/g_d_grn_7.png")
        self.rock0 = py.resource.image("tiles/g_wht_0.png")
        self.rock1 = py.resource.image("tiles/g_wht_1.png")
        self.rock2 = py.resource.image("tiles/g_wht_2.png")
        self.rock3 = py.resource.image("tiles/g_wht_3.png")
        self.rock4 = py.resource.image("tiles/g_wht_4.png")
        self.rock5 = py.resource.image("tiles/g_wht_5.png")
        self.rock6 = py.resource.image("tiles/g_wht_6.png")
        self.rock7 = py.resource.image("tiles/g_wht_7.png")
        self.barren0 = py.resource.image("tiles/g_yelo_0.png")
        self.barren1 = py.resource.image("tiles/g_yelo_1.png")
        self.barren2 = py.resource.image("tiles/g_yelo_2.png")
        self.barren3 = py.resource.image("tiles/g_yelo_3.png")
        self.barren4 = py.resource.image("tiles/g_yelo_4.png")
        self.barren5 = py.resource.image("tiles/g_yelo_5.png")
        self.barren6 = py.resource.image("tiles/g_yelo_6.png")
        self.barren7 = py.resource.image("tiles/g_yelo_7.png")
        self.forest0 = py.resource.image("tiles/g_brn_0.png")
        self.forest1 = py.resource.image("tiles/g_brn_1.png")
        self.forest2 = py.resource.image("tiles/g_brn_2.png")
        self.forest3 = py.resource.image("tiles/g_brn_3.png")
        self.forest4 = py.resource.image("tiles/g_brn_4.png")
        self.forest5 = py.resource.image("tiles/g_brn_5.png")
        self.forest6 = py.resource.image("tiles/g_brn_6.png")
        self.forest7 = py.resource.image("tiles/g_brn_7.png")
        self.prairie_seq = [self.prairie0, self.prairie1, self.prairie2,
                            self.prairie3, self.prairie4, self.prairie5,
                            self.prairie6, self.prairie7]
        self.lush_seq = [self.lush0, self.lush1, self.lush2, self.lush3,
                        self.lush4, self.lush5, self.lush6, self.lush7]
        self.rock_seq = [self.rock0, self.rock1, self.rock2, self.rock3,
                        self.rock4, self.rock5, self.rock6, self.rock7]
        self.barren_seq = [self.barren0, self.barren1, self.barren2,
                            self.barren3, self.barren4, self.barren5,
                            self.barren6, self.barren7]
        self.forrest_seq = [self.forest0, self.forest1, self.forest2,
                            self.forest3, self.forest4, self.forest5,
                            self.forest6, self.forest7]
    def make_tile(self, tile_type,x=0,y=0,frame=-1):
        if tile_type == 'prairie':
            self.make_prarie(x,y,frame)
        elif tile_type == 'lush_prairie':
            self.make_lush(x,y,frame)
        elif tile_type == 'rock':
            self.make_rock(x,y,frame)
        elif tile_type == 'barren':
            self.make_barren(x,y,frame)
        elif tile_type == 'forest':
            self.make_barren(x,y,frame)
        else:
            print('tile type of {tile_type} not a known ground type')
        self.sprite.scale = 2
        self.sprite.scale_x = 1.25
    def make_prarie(self, x=0, y=0, frame = -1):
        if frame == -1:
            frame = random.randint(0,7)
        self.sprite = py.sprite.Sprite(img = self.prairie_seq[frame], x= x, y = y)
    def make_lush(self, x=0, y=0, frame = -1):
        if frame == -1:
            frame = random.randint(0,7)
        self.sprite = py.sprite.Sprite(img = self.lush_seq[frame], x= x, y = y)
    def make_rock(self, x=0, y=0, frame = -1):
        if frame == -1:
            frame = random.randint(0,7)
        self.sprite = py.sprite.Sprite(img = self.rock_seq[frame], x= x, y = y)
    def make_barren(self, x=0, y=0, frame = -1):
        if frame == -1:
            frame = random.randint(0,7)
        self.sprite = py.sprite.Sprite(img = self.barren_seq[frame], x= x, y = y)
    def make_forrest(self, x=0, y=0, frame = -1):
        if frame == -1:
            frame = random.randint(0,7)
        self.sprite = py.sprite.Sprite(img = self.forrest_seq[frame], x= x, y = y)

class Grass:
    def __init__(self):
        self.frame = 0
        self.grass1_0 = py.resource.image("tiles/food_grass1_0.png")
        self.grass1_1 = py.resource.image("tiles/food_grass1_1.png")
        self.grass1_2 = py.resource.image("tiles/food_grass1_2.png")
        self.grass1_3 = py.resource.image("tiles/food_grass1_3.png")
        self.grass1_4 = py.resource.image("tiles/food_grass1_4.png")
        self.grass1_5 = py.resource.image("tiles/food_grass1_5.png")
        self.grass1_6 = py.resource.image("tiles/food_grass1_6.png")
        self.grass1_7 = py.resource.image("tiles/food_grass1_7.png")
        self.grass2_0 = py.resource.image("tiles/food_grass2_0.png")
        self.grass2_1 = py.resource.image("tiles/food_grass2_1.png")
        self.grass2_2 = py.resource.image("tiles/food_grass2_2.png")
        self.grass2_3 = py.resource.image("tiles/food_grass2_3.png")
        self.grass2_4 = py.resource.image("tiles/food_grass2_4.png")
        self.grass2_5 = py.resource.image("tiles/food_grass2_5.png")
        self.grass2_6 = py.resource.image("tiles/food_grass2_6.png")
        self.grass2_7 = py.resource.image("tiles/food_grass2_7.png")
        
        self.grass_seq = [self.grass1_0, self.grass1_1, self.grass1_2,
                            self.grass1_3, self.grass1_4, self.grass1_5,
                            self.grass1_6, self.grass1_7, 
                            self.grass2_0, self.grass2_1, self.grass2_2,
                            self.grass2_3, self.grass2_4, self.grass2_5,
                            self.grass2_6, self.grass2_7]
    def make_tile(self, x=0, y=0,frame=-1):
        if frame == -1:
            frame = random.randint(0,15)
        self.sprite = py.sprite.Sprite(img = self.grass_seq[frame], x= x, y = y)
        self.sprite.scale = 0.50
        self.sprite.scale_x = 0.75 #(0.75, -1.75)[random.randint(0,1)]//requires centered spites
        
class Rock:
    def __init__(self):
        self.frame = 0
        self.rock_0 = py.resource.image("tiles/Stone_0.png")
        self.rock_1 = py.resource.image("tiles/Stone_1.png")
        self.rock_2 = py.resource.image("tiles/Stone_2.png")
        self.rock_3 = py.resource.image("tiles/Stone_3.png")
        self.rock_4 = py.resource.image("tiles/Stone_4.png")
        self.rock_5 = py.resource.image("tiles/Stone_5.png")
        self.rock_6 = py.resource.image("tiles/Stone_6.png")
        self.rock_7 = py.resource.image("tiles/Stone_7.png")
        
        self.rock_seq = [self.rock_0, self.rock_1, self.rock_2, self.rock_3,
                        self.rock_4, self.rock_5, self.rock_6, self.rock_7]
    def make_tile(self, x=0, y=0,frame=-1):
        if frame == -1:
            frame = random.randint(0,7)
        self.sprite = py.sprite.Sprite(img = self.rock_seq[frame], x= x+13, y = y+4)
        self.sprite.scale = 0.3

class Poop:
    def __init__(self):
        self.frame = 0
        self.poop_0 = py.resource.image("tiles/poop_0.png")
        self.poop_1 = py.resource.image("tiles/poop_1.png")
        self.poop_2 = py.resource.image("tiles/poop_2.png")
        self.poop_3 = py.resource.image("tiles/poop_3.png")
        self.poop_4 = py.resource.image("tiles/poop_4.png")
        self.poop_5 = py.resource.image("tiles/poop_5.png")
        self.poop_6 = py.resource.image("tiles/poop_6.png")
        self.poop_7 = py.resource.image("tiles/poop_7.png")
        
        self.poop_seq = [self.poop_0, self.poop_1, self.poop_2, self.poop_3,
                        self.poop_4, self.poop_5, self.poop_6, self.poop_7]
    def make_tile(self, x=0, y=0,frame=-1):
        if frame == -1:
            frame = random.randint(0,7)
        #randomising where poop is
        pos_x = 35 + random.randint(0,10)
        pos_y = 35 + random.randint(0,10)
        self.sprite = py.sprite.Sprite(img = self.poop_seq[frame], x= x + pos_x, y = y + pos_y)
        self.sprite.scale = 0.1

if __name__ == '__main__':
    print(__name__)