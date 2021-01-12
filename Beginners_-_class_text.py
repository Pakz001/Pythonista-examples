
from scene import *
import sound
import random
import math
A = Action

class test:
	x=10
	name = "hello"

class MyScene (Scene):
	def setup(self):
		self.mytest = test()
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		text(str(self.mytest.x),x=200,y=200,font_size=30)
		text(self.mytest.name,x=200,y=250,font_size=30)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
