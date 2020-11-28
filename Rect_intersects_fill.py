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
		r1 = Rect(50,50,200,100)
		r2 = Rect(160,80,100,100)
		banana = False
		if r1.intersects(r2):
			banana=True
		background(1,1,0)
		fill(1,.5,.5,.5)
		rect(r1.x,r1.y,r1.width,r1.height)
		fill(1,0,1,.5)
		rect(r2.x,r2.y,r2.width,r2.height)
		if banana==True:
			tint(0,0,0)
			text('collision',x=100,y=100,font_size=48)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
