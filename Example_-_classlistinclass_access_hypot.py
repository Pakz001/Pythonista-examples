#
# acces lists of objects from within class.
# hypot for distance
# atan2 for angle
#

from scene import *
import sound
import random
import math
A = Action


class agent:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.targetx=0
		self.targety=0
		# set target
	def settarget(self,x,y):
		self.targetx = x
		self.targety = y
		# move this agent to the target and find new
		# target if at destination.
	def movetotarget(self):	
		angle = math.atan2(self.targety-self.y,self.targetx-self.x)
		self.x+= math.cos(angle)*2
		self.y+= math.sin(angle)*2
		# set collision and find new target if arived
		r1 = Rect(self.x-5,self.y-5,10,10)
		r2 = Rect(self.targetx-5,self.targety-5,10,10)
		if r1.intersects(r2):
			self.settarget(random.randint(0,300),random.randint(0,300))
	# look ahead and see if someone is there 
	# adjust target
	def lookaround(self,agent):
		if random.randint(0,100)==0:
			for obj in agent:
				# do not check with itself
				if obj!= self:
					# hypot is used as sqrt to get distance between points
					if math.hypot(obj.targetx-self.x,obj.targety-self.y)<200:
						self.targetx = obj.x
						self.targety = obj.y
		

class MyScene (Scene):
	def setup(self):
		# create our list of agents
		self.a = []
		self.a.append(agent(100,100))
		self.a.append(agent(200,200))
		self.a[0].settarget(300,100)
		self.a[1].settarget(0,0)
		pass
	def did_change_size(self):
		pass
	
	def update(self):
		# move our agents
		for obj in self.a:
			obj.lookaround(self.a)
			obj.movetotarget()			
		pass
		#draw the agents
		for obj in self.a:
			fill(255,0,0)
			rect(obj.x,obj.y,20,20)
			
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
