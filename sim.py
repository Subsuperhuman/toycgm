import vec
import random
import numpy
import math

class Particle:
	mass = 1.0
	velocity = vec.f2(0,0)
	position = vec.f2(0,0)
	lastPostition = vec.f2(0,0)
	force = vec.f2(0,0)

	def __init__(self,mass,velocity,position):
		self.mass = mass
		self.velocity = velocity
		self.position = position

class Simulation:

	particles = []			#main particle array
	xlo = 0					#sim space x lower bound, L/s LJ units
	xhi = 0					#sim space x upper bound, L/s LJ units
	ylo = 0					#sim space y lower bound, L/s LJ units
	yhi = 0					#sim space y upper bound, L/s LJ units
	timestep = 0			#step size for equations of motion
	duration = 0			#duration that the simulation should run for
	vSum = vec.f2(0,0)		#sum of current velocities
	kSum = 0
	vScaleF = 0
	temp = 300				#LJ units - Tk/e
	s = 3.4
	e = 0.238
	rc = 50


	def __init__(self,timestep=0.5,duration=100,xlo=0,xhi=300,ylo=0,yhi=300):
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
		N=100

		for i in range(N):
			self.particles.append(Particle(1.0,vec.f2(0,0),vec.f2(0,0)))

		for p in self.particles:
			p.position.x = random.randrange(self.xlo,self.xhi)
			p.position.y = random.randrange(self.ylo,self.yhi)
			p.velocity.x = random.gauss(0,100)
			p.velocity.y = random.gauss(0,100)
		self.initialiseParticles()

	def calculateGlobalParameters(self):		
		"""an ugly temporary function using stateful parameters"""
		if len(self.particles) > 0:
			self.vSum = vec.f2(0,0)
			self.kSum = 0
			for p in self.particles:
				self.vSum += p.velocity
				self.kSum += p.velocity**2

			self.vSum = self.vSum/float(len(self.particles))
			self.kSum = self.kSum/float(len(self.particles))
			self.vScaleF=math.sqrt(2*self.temp/self.kSum) # two degrees of freedom

	def initialiseParticles(self):
		self.calculateGlobalParameters()
		for p in self.particles:
			p.velocity = (p.velocity - self.vSum)*self.vScaleF
			p.lastPostition = p.position - self.timestep*p.velocity

	def calculateSmallestDistance(self,p,q):
		r = vec.f2(0,0)
		xdiff = p.position.x - q.position.x
		ydiff = p.position.y - q.position.y
		if(xdiff != 0):
			if(abs(xdiff) < abs((self.xhi-self.xlo) - xdiff)):
				r.x = xdiff
			else:
				r.x = -((self.xhi-self.xlo) - xdiff)

		if(ydiff != 0):
			if(abs(ydiff) < abs((self.yhi-self.ylo) - ydiff)):
				r.y = ydiff
			else:
				r.y = -((self.yhi-self.ylo) - ydiff)

		return r

	def calculateLJForce(self,p,q):
		f = vec.f2(0,0)
		r = self.calculateSmallestDistance(p,q)
		if(r.magnitude() < self.rc):
			ri = 1/r.magnitude()
			f = ((48*ri**2)*((ri**12)-0.5*(ri**6)))*r
		return f

	def run(self):
		time = 0
		print("running simulation for " + str(self.duration) + "s with timestep " + str(self.timestep))
		
		while time<self.duration-self.timestep:
			time+=self.timestep
			for p in self.particles:
				p.force = vec.f2(0,0)
			for i in range(len(self.particles)):
				p = self.particles[i]
				for j in range(len(self.particles)-(i+1)):
					q = self.particles[i+j+1]
					p.force += self.calculateLJForce(p,q)
					q.force -= self.calculateLJForce(p,q)

				p.lastPostition = p.position
				p.position += self.timestep*p.velocity
				if(p.position.x > self.xhi):
					p.position.x = self.xlo
				elif(p.position.x < self.xlo):
					p.position.x = self.xhi

				if(p.position.y > self.yhi):
					p.position.y = self.ylo
				elif(p.position.y < self.ylo):
					p.position.y = self.yhi


			self.calculateGlobalParameters()


			#print(self.particles[10].position)
