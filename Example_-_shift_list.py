from scene import *
import sound
import random
import math
A = Action

class MyScene (Scene):
	def setup(self):
		self.time = 0
		self.newvalue = 0
		self.mylist = list(range(5))
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		self.time+=1
		if self.time>60:
			self.time=0
			self.newvalue=random.randint(0,99)
			#here we shift the list insert the new
			#value t the bottom and remove the top value
			self.mylist.pop(0)#remove top index
			self.mylist.append(self.newvalue)#add to the end
				
		text(str(self.newvalue),x=300,y=300,font_size=30)
		for i in range(len(self.mylist)):
			text(str(self.mylist[i]),x=200,y=300+i*20,font_size=20)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
