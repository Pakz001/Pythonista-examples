from scene import *
import sound
import random
import math
A = Action

					
class MyScene (Scene):
	def setup(self):


					
		
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		text(str(random.randint(-10,10)),x=48+100,y=48+100,font_size=20)

		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
