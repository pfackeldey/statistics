import numpy as np
import random as rnd
import matplotlib.pyplot as plt


def M_shaped(x):
	if(-1. <= x <= 1.):
		return (1.+abs(x))
	else:
		return 0.
		

def M_rand(n):
	rnd.seed()
	x=np.array([])
	
	for i in range(n):
		x_rand=np.random.uniform(-1.5,1.5,1)
		y_rand=np.random.uniform(0.,1.5,1)
		if(y_rand<=M_shaped(x_rand)):
			x=np.append(x,x_rand)
			
	return x
	

x=M_rand(100000)

plt.figure(100)
plt.hist(x,bins=200)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("m-shaped distribution")
plt.savefig("m-shaped.png")
#~ plt.show()



to_plot=[1,4,9,19,49]

for i in range(50):
	x_=M_rand(100000)
	x=np.add(x,np.resize(x_,len(x)))
	
	if i in to_plot:
		plt.figure(i)
		plt.hist(x,bins=200)
		plt.xlabel("X")
		plt.ylabel("Y")
		plt.title("m-shaped function stacked "+str(i+1)+" times")
		plt.savefig("m_shaped_function_stacked_"+str(i+1)+".png")
