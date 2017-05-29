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

#line definition:
def line(A,B,x):
	return (B[1]-A[1])/(B[0]-A[0]) * x + 1.

#point on surface:
P = (0.,1.)
count = 0.
n=1000

#TASK A:
fig, (ax,ax1) = plt.subplots(nrows=2, ncols=1)
ax.set_xlim(-1.,1.)
ax.set_ylim(-1.,1.)
ax.set_title("Task a: Chords")

#circle plot:
circle = plt.Circle((0., 0.), 1., fill=False, color='blue')
ax.add_artist(circle)

ax1.set_xlim(-1.,1.)
ax1.set_ylim(-1.,1.)
ax1.set_title("Task a: midpoints")

#circle plot:
circle = plt.Circle((0., 0.), 1., fill=False, color='blue')
ax1.add_artist(circle)

for i in range(n):
	r=np.sqrt(random.random())
	alpha = random.random()*(2*np.pi)
        x,y = r*np.cos(alpha), r*np.sin(alpha)
	new_P1 = (x,y)
	m = (new_P1[1]-P[1])/(new_P1[0]-P[0])
	x1 = -2*m/(m**2+1.)
	y1 = line(new_P1,P,x1)
	new_P2 = (x1,y1)
	if distance(P,new_P2)>side_length(1.):
		count += 1.
		ax.plot([x1,0.],[y1,1.], color = 'red')	
		ax1.plot(x1/2.,(1.+y1)/2., color = 'red', marker = '.')	
	else:
		ax.plot([x1,0.],[y1,1.], color = 'green')
		ax1.plot(x1/2.,(1.+y1)/2., color = 'green', marker = '.')

print "Probability of task a: ",float(count)/float(n)
plt.tight_layout()
plt.grid()
plt.show()


#TASK B:
# P =(1/3*(CIRCLE AREA - TRIANGLE ARE)+TRIANGLE AREA)/CIRCLE AREA
P=(1./3.*(np.pi*1.**2. - np.sqrt(3.)/4. * side_length(1.)**2.)+np.sqrt(3.)/4. * side_length(1.)**2.)/(np.pi*1.**2.)
print "Analytical calculated probability is: ",round(P,3)


#TASK C:
#FIRST METHOD
count = 0.
r=1.

fig, (ax,ax1) = plt.subplots(nrows=2, ncols=1)
ax.set_xlim(-1.,1.)
ax.set_ylim(-1.,1.)
ax.set_title("Bertrand's method 1: Chords")

#circle plot:
circle = plt.Circle((0., 0.), 1., fill=False, color='blue')
ax.add_artist(circle)

ax1.set_xlim(-1.,1.)
ax1.set_ylim(-1.,1.)
ax1.set_title("Bertrand's method 1: midpoints")

#circle plot:
circle = plt.Circle((0., 0.), 1., fill=False, color='blue')
ax1.add_artist(circle)

for i in range(n):
	alpha = random.random()*(2*np.pi)
	x1,y1 = r*np.cos(alpha), r*np.sin(alpha)
	new_P1 = (x1,y1)
	alpha2 = random.random()*(2*np.pi)
	x2,y2 = r*np.cos(alpha2), r*np.sin(alpha2)
	new_P2 = (x2,y2)
	if distance(new_P2,new_P1)>side_length(1.):
		ax.plot([x1,x2],[y1,y2], color = 'red')
		ax1.plot((x2+x1)/2.,(y2+y1)/2., color = 'red', marker = '.')		
		count += 1.
	else:
		ax.plot([x1,x2],[y1,y2], color = 'green')
		ax1.plot((x2+x1)/2.,(y2+y1)/2., color = 'green', marker = '.')
plt.tight_layout()
plt.grid()
plt.show()


print "Probability of first method: ",count/float(n)


#SECOND METHOD
#middle of radius: 
P = (0,1)
count = 0.
r=1.

fig, (ax,ax1) = plt.subplots(nrows=2, ncols=1)
ax.set_xlim(-1.,1.)
ax.set_ylim(-1.,1.)
ax.set_title("Bertrand's method 2: Chords")

#circle plot:
circle = plt.Circle((0., 0.), 1., fill=False, color='blue')
ax.add_artist(circle)

ax1.set_xlim(-1.,1.)
ax1.set_ylim(-1.,1.)
ax1.set_title("Bertrand's method 2: midpoints")

#circle plot:
circle = plt.Circle((0., 0.), 1., fill=False, color='blue')
ax1.add_artist(circle)



for i in range(n):
	# random point on the radius
	m = random.random()*r
	alpha = random.random()*(2*np.pi)
	x,y = m*np.cos(alpha),m*np.sin(alpha)
	M = (x,y)
	beta = alpha-np.pi/2
	length = np.sqrt(pow(r,2)-pow(distance(M,(0,0)),2))
	x1,y1 = x+length*np.cos(beta),y+length*np.sin(beta)
	x2,y2 = x-length*np.cos(beta),y-length*np.sin(beta)
	P1 = (x1,y1)
	P2 = (x2,y2)
	if distance(P1,P2)>side_length(1.):
		ax.plot([x1,x2],[y1,y2], color = 'red')	
		ax1.plot(x,y, color = 'red', marker = '.')		
		count += 1.
	else:
		ax.plot([x1,x2],[y1,y2], color = 'green')
		ax1.plot(x,y, color = 'green', marker = '.')	

plt.tight_layout()
plt.grid()
plt.show()

print "Probability of second method: ",float(count)/float(n)
	

#THIRD METHOD
count = 0.

fig, (ax,ax1) = plt.subplots(nrows=2, ncols=1)
ax.set_xlim(-1.,1.)
ax.set_ylim(-1.,1.)
ax.set_title("Bertrand's method 3: Chords")

#circle plot:
circle = plt.Circle((0., 0.), 1., fill=False, color='blue')
ax.add_artist(circle)

#circle plot:
plt.Circle((0., 0.), 1., fill=False, color='red')

ax1.set_xlim(-1.,1.)
ax1.set_ylim(-1.,1.)
ax1.set_title("Bertrand's method 3: midpoints")

#circle plot:
circle = plt.Circle((0., 0.), 1., fill=False, color='blue')
ax1.add_artist(circle)

for i in range(n):
	#Point on big circle:
	r = np.sqrt(random.random())
	alpha= random.random()*(2*np.pi)
	x,y = r*np.cos(alpha), r*np.sin(alpha)
	P = (x,y)
	
	#chord
	beta = alpha-np.pi/2
	length = np.sqrt(pow(1.,2)-pow(distance(P,(0,0)),2))
	x1,y1 = x+length*np.cos(beta),y+length*np.sin(beta)
	x2,y2 = x-length*np.cos(beta),y-length*np.sin(beta)
	P1 = (x1,y1)
	P2 = (x2,y2)
	
	#Point on small circle:
	r_small = 1./2.
	x3,y3 = r_small*np.cos(alpha), r_small*np.sin(alpha)
	P3 = (x3,y3)
	if distance(P,(0.,0.))<distance(P3,(0.,0.)):
		ax.plot([x1,x2],[y1,y2], color = 'red')	
		ax1.plot(x,y, color = 'red', marker = '.')	
		count += 1.
	else:
		ax.plot([x1,x2],[y1,y2], color = 'green')
		ax1.plot(x,y, color = 'green', marker = '.')

plt.tight_layout()
plt.grid()
plt.show()

print "Probability of third method: ",float(count)/float(n)		
