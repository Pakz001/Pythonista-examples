from scene import *
import sound
import random
import math
A = Action

class balldrick:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class MyScene (Scene):
	def setup(self):
		self.angle = 0
		self.bx = 200
		self.by = 200
		self.fly = []
		self.fly.append(balldrick(self.bx,self.by))
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		# increase the angle
		self.angle+=.1
		#if the angle is greater than 2xpi(full circle)
		if self.angle>math.pi*2:
			self.angle=0#angle back to 0
		#update our position
		self.bx += math.cos(self.angle)*5
		self.by += math.sin(self.angle)*5
		#put the new position on the list
		self.fly.append(balldrick(self.bx,self.by))
		#if our trail is longer than 10 than remove top(last inserted)
		if len(self.fly)>10:
			self.fly.pop(0)#remove top index
		# draw the trail
		for obj in self.fly:
			fill(255,255,255)
			rect(obj.x,obj.y,32,32)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
