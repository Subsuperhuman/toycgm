import math

""" vector classes for toycgm """

class f2:
	""" a 2 dimensional floating point vector """
	x=0.0
	y=0.0

	def __init__(self,x=0.0,y=0.0):
		self.x = x
		self.y = y

	def magnitude(self):
		""" returns the magnitude of the vector """
		return math.sqrt(self.x*self.x+self.y*self.y)

	def normal(self):
		""" returns a right handed normal vector """
		return Vec2(-self.x,self.y)

	def normalise(self):
		""" returns a unit vector in the direction of the vector """
		rMag = 1.0/self.magnitude()
		return Vec2(-self.x*rMag,self.y*rMag)

	def arg(self):
		""" returns the argument in radians """
		arg = math.acos(f2(0,1)*self/self.magnitude())
		return arg if arg >= 0 else arg + 2*math.PI

	def __add__(self,other):
		""" vector addition """
		return f2(self.x+other.x,self.y+other.y)

	def __add__(self,other):
		""" vector subtraction """
		return f2(self.x-other.x,self.y-other.y)

	def __mul__(self,other):
		""" dot product """
		if type(self) == type(other):
			return f2(self.x*other.x,self.y*other.y)
		elif other==float(other):
			return  f2(float(other)*self.x,float(other)*self.y)

	def __rmul__(self,other):
		""" for prefixed multiplications """
		return self.__mul__(other)

	def __repr__(self):
		""" for the interactive console or reflection debugging """
		return "vecf2 - " + str(self)

	def __str__(self):
		""" for printing """
		return "(" + str(self.x) + "," + str(self.y) + ")"



