from scene import *
import sound
import random
import math
A = Action

class MyScene (Scene):
	def setup(self):
		button_font = ('Avenir Next', 20)
		self.title_label = LabelNode("hello world", font=button_font, color='white', position=(self.size.x/2,self.size.y/2), parent=self)
		
		self.grid = [[None] * 10 for y in range(10)]
		self.grid[5][5]=5
		self.txt = LabelNode(str(self.grid[5][5]),font=button_font, color='white', position=(self.size.x/2,self.size.y/2+50), parent=self)
		
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
