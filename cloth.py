import pyglet
from visual import *
 
class Physics:

	def applyForce(force):
		acceleration = acceleration + (force/mass)
        ball=sphere(pos=vector(4,7,3),radius=2,color=color.green)

class HelloWorldWindow(pyglet.window.Window): #creates a class that inherits from 'Window'
    def __init__(self):
        super(HelloWorldWindow, self).__init__() #runs the 'Window' constructor
        self.label = pyglet.text.Label('Hello, world!') #creates a 'Label' instance
 
    def on_draw(self): #!#!defines an 'on_draw' function for 'HelloWorldWindow', this will run every frame!#!#
        self.clear() #clears the screen
        self.label.draw() #blits the label to the screen
 
if __name__ == '__main__': #only runs if this file is run by itself, not from an import
    window = HelloWorldWindow() #creates an instance of 'HelloWorldWindow'
    pyglet.app.run() #starts the pyglet event loop (which starts the application)