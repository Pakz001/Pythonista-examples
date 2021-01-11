from scene import *
import sound
import random
import math
A = Action

					
class MyScene (Scene):
	def setup(self):

		self.grid = [[None] * 50 for y in range(50)]
		x=25
		y=25
		for i in range(500):
			z = random.randint(0,3)
			if z==0:
				x+=1
			if z==1:
				y+=1
			if z==2:
				x-=1
			if z==3:
				y-=1
			if x<0:
				x=0
			if x>49:
				x=49
			if y<0:
				y=0
			if y>49:
				y=49
			self.grid[y][x]=1
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		for y in range(50):
			for x in range(50):
				if self.grid[y][x]==1:
					rect(x*16, y*10+100, 16,10)

		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
