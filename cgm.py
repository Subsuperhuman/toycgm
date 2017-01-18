import vec

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

	def __init__(self):
		self.particles.append(Particle(1.0,vec.f2(1.0,1.0),vec.f2(1.0,1.0)))

	def run(self):
		for p in self.particles:
			print(p.velocity.magnitude())



def main():
	simulation = Simulation()
	simulation.run()

if __name__ == "__main__":
	main()