#!/usr/bin/python
import numpy as np
import random
from matplotlib import pyplot as plt

#FIRST METHOD
#distance between 2 points:
def distance(A,B):
	return np.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)

#length of triangle side:
def side_length(r):
	return 3*r/np.sqrt(3) #from geometrics



#point on surface:
P = (0.,1.)
count = 0.
n=1000
r=1.

for i in range(n):
	alpha = random.random()*(2*np.pi)
        x,y = r*np.cos(alpha), r*np.sin(alpha)
	new_P = (x,y)
	print distance(P,new_P)
	if distance(P,new_P)>side_length(1.):
		count += 1.
	else:
		pass


print "Result of first method: ",count/float(n)

#SECOND METHOD

	














	
