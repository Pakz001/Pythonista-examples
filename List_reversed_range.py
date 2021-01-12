
from scene import *
import sound
import random
import math
A = Action

class MyScene (Scene):
	def setup(self):
		#list(reversed(range(0, 5)))
		self.mylist1 = list(range(5))
		self.mylist2 = list(reversed(range(5)))
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		y=0
		for i in range(len(self.mylist1)):
			text(str(self.mylist1[i]),x=300,y=300+y,font_size=30)
			y+=30
		y=0
		for i in range(len(self.mylist2)):
			text(str(self.mylist2[i]),x=400,y=300+y,font_size=30)
			y+=30
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
