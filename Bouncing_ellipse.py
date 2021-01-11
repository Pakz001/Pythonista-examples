from scene import *
import sound
import random
import math
A = Action

					
class MyScene (Scene):
	def setup(self):
		self.bx = 500
		self.by = 300
		self.incy = 8
		self.incmod = 0.1
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		fill(255,255,255)
		ellipse(self.bx,self.by,100,100)
		self.by += self.incy
		self.incy-=self.incmod
		if self.incy<-8:
			self.incy=8
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
