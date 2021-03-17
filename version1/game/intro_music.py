import pyglet as py
#set up resource path
# py.resource.path = ['./resources']
# py.resource.reindex()

#set audio driver options
py.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

#reference song files and load them
intro = py.media.load("./resources/intro.wav")

#play intro
intro.play()

py.app.run()

#works as is if run directly from this file


