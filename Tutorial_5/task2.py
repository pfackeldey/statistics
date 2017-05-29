#!/usr/bin/python
import numpy as np
import random
from matplotlib import pyplot as plt


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

#TASK A:
for i in range(n):
	r=random.random()
	alpha = random.random()*(2*np.pi)
        x,y = r*np.cos(alpha), r*np.sin(alpha)
	new_P = (x,y)
	if distance(P,new_P)>side_length(1.):
		count += 1.
	else:
		pass


print "Result of task a: ",count/float(n)



#TASK C:
#FIRST METHOD
P = (0.,1.)
count = 0.
n=1000
r=1.

for i in range(n):
	alpha = random.random()*(2*np.pi)
        x,y = r*np.cos(alpha), r*np.sin(alpha)
	new_P = (x,y)
	if distance(P,new_P)>side_length(1.):
		count += 1.
	else:
		pass


print "Result of first method: ",count/float(n)

#SECOND METHOD

P = (0.,1.)
count = 0.
n=10000
r=1.

for i in range(n):
	alpha = random.uniform(-0.5,0.5)*(np.pi)
	beta = 2*alpha+np.pi
        x1,y1 = r*np.cos(alpha), r*np.sin(alpha)
	x2,y2 = r*np.cos(beta), r*np.sin(beta)
	new_P1 = (x1,y1)
	new_P2 = (x2,y2)
	if distance(new_P1,new_P2)>side_length(1.):
		count += 1.
	else:
		pass	

print "Result of second method: ",float(count)/float(n)












	
