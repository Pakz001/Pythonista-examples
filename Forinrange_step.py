
from scene import *
import sound
import random
import math
A = Action

class MyScene (Scene):
	def setup(self):
		self.z = 0
		for i in range(10,20,5):#i goes from 10 to 19
			self.z+=1
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		text(str(self.z),x=320,y=320,font_size=50)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
