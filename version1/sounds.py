import pyglet as py
import random

# set audio driver options
py.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
# py.resource.path = ['./resources/sounds']
# py.resource.reindex()
poop1 = py.resource.media("sounds/poop.wav", streaming=False)
intro = py.resource.media("sounds/intro_track.wav", streaming=False)
jump = py.resource.media("sounds/Jump.wav", streaming=False)
nature = py.resource.media("sounds/nature_background.wav", streaming=False)
eat = py.resource.media("sounds/Eating.wav", streaming=False)
bonk = py.resource.media("sounds/bonk.wav", streaming=False)

class Sound:
    def __init__(self):
        self.poops = [poop1]
        self.intro = [intro]
        self.nature = [nature]
        self.jump = [jump]
        self.eat = [eat]
        self.bonk = [bonk]

    def playSound(self, category):
        if len(self.category) == 0:
            return -1
        elif len(self.category) == 1:
            self.category[0].play()
        else:
            random.choice(self.category).play()
            


