
from scene import *
import sound
import random
import math
A = Action

					
class MyScene (Scene):
	def setup(self):
		self.touchx = 0
		self.touchy = 0
		self.touchendx = 0
		self.touchendy = 0

		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		#text(str(self.touchx)+","+str(self.touchy),x=320,y=200,font_size=32)
		#color of line r,g,b(0..255)
		stroke(255,255,255)
		#thickness of line
		stroke_weight(4)
		#line xy to xy
		line(0,0,200,200)
		
		pass
	
	def touch_began(self, touch):
		self.touchx,self.touchy = touch.location
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		self.touchendx,self.touchendy = touch.location
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
