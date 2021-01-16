
from scene import *
import sound
import random
import math

A = Action


class ui:
	def __init__(self,x,y):
		self.top = y
		self.left = x
		self.bw = 96
		self.bh = 128
		self.pointsleft = 0
		self.touchx = 0
		self.touchy = 0
		self.listindex=0
		self.list = []
		for i in range(32):
			self.list.append(random.randint(20,100))
	def update(self,touchx,touchy):
		self.touchx = touchx
		self.touchy = touchy
		if self.isbuttonpressedup():
			self.pointsleft+=1
			self.list[self.listindex]-=1
		if self.isbuttonpresseddown():
			self.pointsleft-=1
			self.list[self.listindex]+=1
		for y in range(2,10):
			#fill(.5,.5,.5,1)
			#rect(self.left-160,y*50,160,60)
			x=self.left-160
			r1=Rect(self.touchx,self.touchy,1,1)
			r2=Rect(x,y*50,160,60)
			if r1.intersects(r2):
				self.top=y*50-self.bh/3
				self.listindex=y
		pass
	def isbuttonpressedup(self):
		r1=Rect(self.touchx,self.touchy,1,1)
		r2=Rect(self.left,self.top,self.bw,self.bh/2)
		if r1.intersects(r2):
			return True
		pass
	def isbuttonpresseddown(self):
		r1=Rect(self.touchx,self.touchy,1,1)
		r2=Rect(self.left,self.top+self.bh/2,self.bw,self.bh/2)
		if r1.intersects(r2):
			return True
		pass
	def draw(self):
		fill(.1,.1,.1,1)
		rect(self.left,self.top+self.bh/2-10,self.bw,20)
		stroke(255,255,255)
		stroke_weight(4)
		x=self.left
		y=self.top
		w=self.bw
		h=self.bh
		#bottom arrow(top in code)
		line(x,y+h/2+15,x+w,y+h/2+15)
		line(x,y+h/2-15,x+w/2,y)
		line(x+w,y+h/2-15,x+w/2,y)
		#top arrow(bottom in code)
		line(x,y+h/2-15,x+w,y+h/2-15)
		line(x,y+h/2+15,x+w/2,y+h)
		line(x+w,y+h/2+15,x+w/2,y+h)
		fill(1,1,1,1)
		text(str(self.pointsleft),x=self.left+self.bw/2,y=self.top+self.bh/2,font_size=20)
		for y1 in range(2,10):
			fill(.5,.5,.5,1)
			rect(self.left-160,y1*50,160,60)
			fill(1,1,1,1)
			text(str(self.list[y1]),x=self.left-100,y=y1*50+25,font_size=20)
					
class MyScene (Scene):
	def setup(self):
		self.myui = ui(160,110)
		self.touchx = 0
		self.touchy = 0
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		self.myui.draw()
		self.myui.update(self.touchx,self.touchy)
		self.touchx = -1
		self.touchy = -1
		fill(1,1,1,1)
		text("Daggerfall class stats menu part",x=200,y=20,font_size=20)
		pass
	
	def touch_began(self, touch):
		self.touchx,self.touchy = touch.location
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		self.touchendx,self.touchendy = touch.location
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
