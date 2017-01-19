""" External libraries """
import argparse

""" Internal libraries """
import sim


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--seed','-s', dest='seed', required=False,
                  	default=None,
                    help='add a seed to the RNG in the simulation')
parser.add_argument('--in','-i', dest='filepath', required=False,
                  	default=None,
                    help='set path for input JSON data file')
parser.add_argument('--out','-o', dest='dumppath', required=False,
                  	default="out.dat",
                    help='set path for output file - defaults to out.dat')

args = parser.parse_args()

def main():
	simulation = sim.Simulation()
	if(args.seed != None):
		simulation.seed(args.seed)
	simulation.initialise()
	simulation.run()

if __name__ == "__main__":
	main()