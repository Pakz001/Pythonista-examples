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
		fill(0,0,0)
		ellipse(50,50,50,50)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
