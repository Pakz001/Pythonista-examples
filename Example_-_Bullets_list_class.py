
from scene import *
import sound
import random
import math
A = Action

class test:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.incx = random.uniform(-2,2)
		self.incy = random.uniform(-2,2)
		self.countdown=random.randint(100,200)
	def update(self):
		self.x+=self.incx
		self.y+=self.incy
		self.countdown-=1
class MyScene (Scene):
	def setup(self):
		self.bullet = []
		for i in range(10):
			self.bullet.append(test(200,200))
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		while(len(self.bullet)<10):
			self.bullet.append(test(200,200))
		for obj in self.bullet:
			obj.update()
			if(obj.countdown<0):
				self.bullet.remove(obj)
		for obj in self.bullet:
			fill(255,255,255)
			ellipse(obj.x,obj.y,32,32)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
