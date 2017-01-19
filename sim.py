import vec
import random
import numpy

class Particle:
	mass = 1.0
	velocity = vec.f2(0.0,0.0)
	position = vec.f2(0.0,0.0)

	def __init__(self,mass,velocity,position):
		self.mass = mass
		self.velocity = velocity
		self.position = position

class Simulation:

	particles = []
	xlo = 0
	xhi = 0
	ylo = 0
	yhi = 0
	timestep = 0
	duration = 0

	def __init__(self,timestep=0.05,duration=100,xlo=0,xhi=300,ylo=0,yhi=300):
		print("setting up a ["+str(xhi-xlo) + " x " + str(yhi-ylo) +"] space")
		self.xlo=xlo
		self.xhi=xhi
		self.ylo=ylo
		self.yhi=yhi
		self.timestep=timestep
		self.duration=duration

	def seed(self,seed=0):
		print("seeding RNG with value " + str(seed))
		random.seed(seed)

	def initialise(self):
		print("adding N particles")
		for p in self.particles:
			p.velocity.x = random.gauss(0,100)
			p.velocity.y = random.gauss(0,100)

	def run(self):
		time = 0
		print("running simulation for " + str(self.duration) + "s with timestep " + str(self.timestep))
		
		while time<self.duration-self.timestep:
			time+=self.timestep
			print(str(time))
			for p in self.particles:
				print(p.velocity)
