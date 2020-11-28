from scene import *
import ui
import sound
import random
import math
A = Action

from PIL import Image, ImageDraw



class MyScene (Scene):
	

			
	def setup(self):
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		background(1,1,0)
		tint(1,1,1)
		rect(50,50,200,100)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
