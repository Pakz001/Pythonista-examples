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
		text('hello' ,x=100, y=100, font_size=48)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
