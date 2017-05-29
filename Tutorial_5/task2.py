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
	r=np.sqrt(random.random())
	alpha = random.uniform(-0.5,0.5)*(2*np.pi)
        x,y = r*np.cos(alpha), r*np.sin(alpha)
	new_P = (x,y)
	if distance(P,new_P)>side_length(1.):
		count += 1.
	else:
		pass

print "Result of task a: ",count/float(n)

#TASK B:
# P =1/3 * (CIRCLE AREA - TRIANGLE ARE)/CIRCLE AREA
P=1./3. * (np.pi*1.**2. - np.sqrt(3.)/4. * side_length(1.)**2.)/(np.pi*1.**2.)
print "Analytical calculated probability is: ",P


#TASK C:
#FIRST METHOD
count = 0.
r=1.
plt.figure(1)

for i in range(n):
	alpha = random.random()*(2*np.pi)
	x1,y1 = r*np.cos(alpha), r*np.sin(alpha)
	new_P = (x1,y1)
	alpha2 = random.random()*(2*np.pi)
	x2,y2 = r*np.cos(alpha2), r*np.sin(alpha2)
	new_P2 = (x2,y2)
	if distance(new_P2,new_P)>side_length(1.):
		plt.plot([x1,x2],[y1,y2], color = 'red')		
		count += 1.
	else:
		plt.plot([x1,x2],[y1,y2], color = 'green')

#circle plot:
plt.Circle((0, 0), 1., fill=False, color='blue')
#triangle plot:
plt.grid()
plt.show()


print "Result of first method: ",count/float(n)


#SECOND METHOD
#middle of radius: 
P = (0,1)
count = 0.
r=1.

plt.figure(2)

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
		plt.plot([x1,x2],[y1,y2], color = 'red')		
		count += 1.
	else:
		plt.plot([x1,x2],[y1,y2], color = 'green')

#circle plot:
plt.Circle((0, 0), 1., fill=False, color='blue')
#triangle plot:
plt.grid()
plt.show()

print "Result of second method: ",float(count)/float(n)
	

#THIRD METHOD
count = 0.

plt.figure(1)

for i in range(n):
	#Point on big circle:
	r = np.sqrt(random.random())
	alpha= random.random()
	x1,y1 = r*np.cos(alpha), r*np.sin(alpha)
	P1 = (x1,y1)
	#Point on small circle:
	r_small = 1/2.
	x2,y2 = r_small*np.cos(alpha), r_small*np.sin(alpha)
	P2 = (x2,y2)
	if distance(P1,(0.,0.))<distance(P2,(0.,0.)):
		plt.plot([x1,x2],[y1,y2], color = 'red')		
		count += 1.
	else:
		plt.plot([x1,x2],[y1,y2], color = 'green')

#circle plot:
plt.Circle((0, 0), 1., fill=False, color='blue')
#triangle plot:
plt.grid()
plt.show()

print "Result of third method: ",float(count)/float(n)	









	
