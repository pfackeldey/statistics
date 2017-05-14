import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from PIL import Image


def elephant_function(n):

	picture=Image.open("elephant.bmp")
	pixels=picture.load()

	width,height=picture.size

	rnd.seed()

	x=np.array([])
	y=np.array([])

	for i in range(n):
		x_rand=np.random.uniform(0,width,1)
		y_rand=np.random.uniform(0,height,1)
		
		color_value=pixels[int(x_rand),int(y_rand)]
		
		not_white=1
		
		for i in xrange(3):
			if (color_value[i]==255):
				not_white=not_white*0
		
		if(not_white == 1):
			x=np.append(x,x_rand)
			y=np.append(y,y_rand)
	
	y=height-y
		
	return x,y

x,y=elephant_function(50000)
plt.figure(100)
plt.hist2d(x,y,bins=250)
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar()
plt.title("elephant function")
plt.savefig("elephant_function.png")

to_plot=[1,4,9,19,49]

for i in range(50):
	x_,y_=elephant_function(20000)
	x=np.add(x,np.resize(x_,len(x)))
	y=np.add(y,np.resize(y_,len(y)))
	
	if i in to_plot:
		plt.figure(i)
		plt.hist2d(x,y,bins=250)
		plt.xlabel("X")
		plt.ylabel("Y")
		plt.colorbar()
		plt.title("Elephant function stacked "+str(i+1)+" times")
		plt.savefig("Elephant_function_stacked_"+str(i+1)+".png")
	
