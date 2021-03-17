import pyglet as py
#set up resource path
# py.resource.path = ['./resources']
# py.resource.reindex()

#set audio driver options
py.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

#reference song files and load them
intro = py.media.load("./resources/intro.wav")
nature = py.media.load("./resources/nature_background.wav")
#play intro
background_player = py.media.Player()
background_player.eos_action = py.media.SourceGroup.loop
background_player.queue(nature)
background_player.eos_action = py.media.SourceGroup.loop
# intro.play()
# nature.play()
background_player.play()
py.app.run()

#works as is if run directly from this file


