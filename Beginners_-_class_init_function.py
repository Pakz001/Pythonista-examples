
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
	def __init__(self):
		self.x=10
		self.name = "hello"
	def ding(self):
		self.x=50

class MyScene (Scene):
	def setup(self):
		self.mytest = test()#create class in mytest
		self.mytest.ding()#call function in class
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		text(str(self.mytest.x),x=200,y=200,font_size=30)
		text(self.mytest.name,x=200,y=250,font_size=30)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
