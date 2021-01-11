from scene import *
import sound
import random
import math
A = Action

					
class MyScene (Scene):
	def setup(self):
		self.touchx = 0
		self.touchy = 0

		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		text(str(self.touchx)+","+str(self.touchy),x=320,y=200,font_size=32)

		pass
	
	def touch_began(self, touch):
		self.touchx,self.touchy = touch.location
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
