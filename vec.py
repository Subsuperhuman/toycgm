import math

class f2:
	x=0.0
	y=0.0

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def magnitude(self):
		return math.sqrt(self.x*self.x+self.y*self.y)

	def normal(self):
		return Vec2(-self.x,self.y)

	def unit(self):
		rMag = 1.0/self.magnitude()
		return Vec2(-self.x*rMag,self.y*rMag)