import pyglet as py
import random

# set audio driver options
py.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
# py.resource.path = ["../resources"]
# py.resource.reindex()
poop1 = py.media.load("./resources/sounds/poop.wav", streaming=False)
intro = py.media.load("./resources/sounds/intro_track.wav", streaming=False)
jump = py.media.load("./resources/sounds/Jump.wav", streaming=False)
nature = py.media.load("./resources/sounds/nature_background.wav", streaming=False)
eat = py.media.load("./resources/sounds/Eating.wav", streaming=False)
bonk = py.media.load("./resources/sounds/bonk.wav", streaming=False)


class Sound:
    #initializes sound class with pre loaded media resources in their respective list 'categories'
    def __init__(self):
        self.sounds = {
            'poops': [poop1],
            'intro': [intro],
            'nature': [nature],
            'jump': {
                'tile_type1' : intro,
                'tile_type2' : jump,
                'tile_type3' : jump,
                'tile_type4' : jump
            },
            'eat': [eat],
            'bonk': [bonk]        
        }

    def playSound(self, category):
        """if only one item in category, play that sound. if more, pick a random sound byte in that category to play"""
        if len(self.sounds[category]) == 0:
            return -1
        elif len(self.sounds[category]) == 1:
            self.sounds[category][0].play()
        else:
            random.choice(self.sounds[category]).play()

    def playJump(self, tile_type, category='jump' ):
        '''Plays a tile specific sound'''
        sound = self.sounds[category][tile_type]
        sound.play()
            
if __name__ == '__main__':       
    sounds = Sound()
    sounds.playJump('tile_type1', 'jump')
    py.app.run()
    
