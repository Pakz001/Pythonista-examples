
from scene import *
import sound
import random
import math
A = Action

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

class test:
	def __init__(self,a):
		self.x=10
		self.name = a
	def ding(self):
		self.x=50

class MyScene (Scene):
	def setup(self):
		self.a = []
		self.a.append(test("banana"))
		self.a.append(test("berry"))
		pass
	def did_change_size(self):
		pass
	
	def update(self):
		y=0
		for obj in self.a:
			text(obj.name,x=200,y=200+y,font_size=20)
			y+=20
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
