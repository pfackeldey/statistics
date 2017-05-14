#!/usr/bin/python
import numpy as np
import random
import argparse

parser = argparse.ArgumentParser(description='Calculate pi.')
parser.add_argument('-n','--number-randomed', type=int, help='Number of random generated x and y. (recommended: n>1000)')

args = parser.parse_args()

#radius of circle:
def radius(x,y):
	return np.sqrt(x**2+y**2)



#checking if it (x,y random distributed) is in the circle:


circle_hits=0.

for i in xrange(args.number_randomed):
	x=random.random()
	y=random.random()
	if (radius(x,y)<1.):
		circle_hits+=1.
	else:
		pass

#calculate pi (only quarter of circle)
def pi(circle_hits,everything):
	return 4*circle_hits/everything

print "Calculating pi with the circle method results in:"
print "pi=",pi(float(circle_hits),float(args.number_randomed))
