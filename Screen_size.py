from scene import *
import ui
import sound
import random
from random import randint
import math
A = Action

from PIL import Image, ImageDraw



class MyScene (Scene):
	

			
	def setup(self):
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		w='Screen width :{0}'.format(size().width)
		h='Screen height :{0}'.format(size().height)
		text(w,x=300,y=100,font_size=48)
		text(h,x=300,y=60,font_size=48)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
