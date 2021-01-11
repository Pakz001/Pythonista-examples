from scene import *
import sound
import random
import math
A = Action

class MyScene (Scene):
	def setup(self):

		
		self.grid = [[None] * 10 for y in range(10)]
		self.grid[5][5]=5
	
		
		for x in range(10):
			self.grid[0][x]=x
			self.grid[9][x]=9-x
		
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		for y1 in range(10):
			for x1 in range(10):
				text(str(self.grid[y1][x1]),x=x1*48+100,y=y1*48+100,font_size=20)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
