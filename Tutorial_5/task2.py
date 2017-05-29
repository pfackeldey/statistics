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

#TASK B:
# P = 1/3 * (CIRCLE AREA - TRIANGLE ARE)



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
#middle of radius: 
P = (0,1)
count = 0.
n=1000
r=1.

alpha = random.random()*(2*np.pi)
beta = abs(alpha-np.pi/2)
r_mid = (r/2*np.cos(alpha), r/2*np.sin(alpha))
for i in range(n):
	# random point on the radius
	m = random.random()*r
	x,y = m*np.cos(alpha),m*np.sin(alpha)
	M = (x,y)
	length = np.sqrt(pow(r,2)-pow(distance(M,(0,0)),2))
	x1,y1 = x+length*np.cos(beta),y+length*np.sin(beta)
	x2,y2 = x-length*np.cos(beta),y-length*np.sin(beta)
	P1 = (x1,y1)
	P2 = (x2,y2)
	if distance(P1,P2)>side_length(1.):
		count += 1.
	else: 
		pass

print "Result of second method: ",float(count)/float(n)
	

#THIRD METHOD
P = (0,1)
count = 0.
n=1000
r=1.










	
