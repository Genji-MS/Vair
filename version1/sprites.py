import pyglet as py

class Title_Rabbit:
    def __init__(self):
        self.frame = 0
        self.frameMAX = 8
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

class Sprite_Rabbit:
    def __init__(self):
        self.frame = 0
        self.frameMAX = 8
        self.flip = False
        self.x = 325
        self.y = 250
        self.scale_x = 1
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
                        self.nom4, self.nom5, self.ded0, self.ded1,
                        self.ded2, self.ded3, self.ded4, self.ded5,
                        self.ded6, self.ded7]
        self.update(0)
    def update(self, _):
        #clock sends a parameter. '_' used (as in GO) to denote a variable we don't use
        self.frame += 1 #increments the array to use the next image %(mod) the length of the array
        if self.frame == self.frameMAX == 16 or self.frame == self.frameMAX == 24:
            #resets our jumping frame cycle back to idle animation
            self.frameMAX = 8
        elif self.frame == self.frameMAX == 38:
            #resets our eating cycle to idle
            self.frameMAX = 8
            #fix the eat from being reversed
            if self.scale_x > 0:
                self.scale_x = -1
            else:
                self.scale_x = 1
        # add for dead animation

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
    def hop_out(self, ro = 'X'):
        if self.frameMAX == 8:
            if ro == 'L':
                self.scale_x = -1
            elif ro == 'R':
                self.scale_x = 1
            self.frame = 8
            self.frameMAX = 16
    def hop_in(self, ro = 'X'):
        if self.frameMAX == 8:
            if ro == 'L':
                self.scale_x = -1
            elif ro == 'R':
                self.scale_x = 1
            self.frame = 16
            self.frameMAX = 24
    def nom(self):
        if self.frameMAX == 8:
            if self.scale_x > 0:
                self.scale_x = -1
            else:
                self.scale_x = 1
            self.frame = 24
            self.frameMAX = 38


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

if __name__ == '__main__':
    print(__name__)