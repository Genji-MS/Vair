import pyglet as py
# set up resource path
# py.resource.path = ['./resources']
# py.resource.reindex()

# set audio driver options
py.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

<<<<<<< HEAD

if __name__ == '__main__':
    nature = py.media.load("./resources/sounds/nature_background.wav", streaming=False)
    poop_sound = py.media.load("./resources/sounds/poop.wav", streaming = False)
    #play intro
    background_player = py.media.Player()
    background_player.loop = True
    background_player.queue(nature)
    background_player.play()
    input("press enter")
    poop_sound.play()
    input("press enter")
    poop_sound.play()
    input("press enter")
    poop_sound.play()
    input("press enter")
    poop_sound.play()
    py.app.run()

    #works as is if run directly from this file


=======

# reference song files and load them
intro = py.media.load("./resources/sounds/intro.wav")
nature = py.media.load("./resources/nature_background.wav")
# play intro
background_player = py.media.Player()
background_player.eos_action = py.media.SourceGroup.loop
background_player.queue(nature)
background_player.eos_action = py.media.SourceGroup.loop
# intro.play()
# nature.play()
background_player.play()
py.app.run()

# works as is if run directly from this file
>>>>>>> d9a2f49b28959173aa110db636adb6ebf0354eaf
