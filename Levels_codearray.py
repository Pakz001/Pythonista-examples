from scene import *
import sound
import random
import math
A = Action

					
class MyScene (Scene):
	def setup(self):
		self.LEVELS = [	["12345",
										"54321",
										"00000",
										"00000",
										"00000"],
										
										["99999",
										"88888",
										"00000",
										"00000",
										"00000"]
										
										]

					
		
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		text(str(self.LEVELS[0][0][1]),x=48+100,y=48+100,font_size=20)
		text(str(self.LEVELS[1][0][1]),x=48+100,y=48+200,font_size=20)
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
