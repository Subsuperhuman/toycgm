class Vec2:
	x=0.0
	y=0.0

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def magnitude(self):
		return self.x*self.x+self.y*self.y

	def normal(self):
		return Vec2(-self.x,self.y)

	def unit(self):
		rMag = 1.0/self.magnitude()
		return Vec2(-self.x*rMag,self.y*rMag)

class Particle:
	mass = 1.0
	velocity = Vec2(0.0,0.0)
	position = Vec2(0.0,0.0)

	def __init__(self,mass,velocity,position):
		self.mass = mass
		self.velocity = velocity
		self.position = position

class Simulation:

	particles = []

	def __init__(self):
		self.particles.append(Particle(1.0,Vec2(1.0,1.0),Vec2(1.0,1.0)))

	def run(self):
		for p in self.particles:
			print(p.mass)



def main():
	simulation = Simulation()
	simulation.run()

if __name__ == "__main__":
	main()