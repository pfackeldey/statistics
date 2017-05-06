#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import interpolate
#open data
data = open("data.txt", "r")

#read data and save it in np arrays
get_data = [line.strip().split() for line in data]

print get_data

xdata=np.array([])
ydata=np.array([])

for i in range(len(get_data)):
	x = get_data[i][0]	
	y = get_data[i][1]
	xdata=np.append(xdata,np.float64(x))
	ydata=np.append(ydata,np.float64(y))
print xdata
print ydata
data.close()


#linear interpolation
def interpolate(x):
	yref=np.array([])
	for entry in x:
		index1=0
		index2=0
		if(entry<xdata[0]):
			index1=0
			index2=1
		if(entry>xdata[len(xdata)-1]):
			index1=len(xdata)-2
			index2=len(xdata)-1
		for i in range(1,len(xdata)):
			if(entry>xdata[i-1])and(entry<xdata[i]):
				index1=i-1
				index2=i
		slope=(ydata[index2]-ydata[index1])/(xdata[index2]-xdata[index1])
		b=ydata[index1]-slope*xdata[index1]
		y=slope*entry+b	
		yref=np.append(yref,float(y))
	return yref


xref=np.arange(-2.15,4.05,0.05)
print xref

yref=interpolate(xref)

a=np.zeros(len(xdata)-1)
b=np.zeros(len(xdata))
c=np.zeros(len(xdata)-1)
F=np.zeros(len(xdata))

matrix=np.zeros((len(xdata),len(xdata)))

#cubic interpolation
for i in range(1,len(xdata)-1):
	a[i]=1./6.*(xdata[i]-xdata[i-1])
	matrix[i-1][i]=a[i]
for i in range(1,len(xdata)-1):		
	b[0]=1./3.*(xdata[1]-xdata[0])#boundary conditions	
	b[i]=1./3.*(xdata[i+1]-xdata[i-1])
	matrix[i-1][i+1]=b[i]
for i in range(len(xdata)-2):
	c[i]=1./6.*(xdata[i+1]-xdata[i])
	matrix[i+1][i]=c[i]
for i in range(1,len(xdata)-2):
	F[i]=(ydata[i+1]-ydata[i])/(xdata[i+1]-xdata[i])-(ydata[i]-ydata[i-1])/(xdata[i]-xdata[i-1])
	
matrix[0][0]=b[0]
F[0]=0.
F[-1]=0.
F.transpose()
print matrix
print F
	
def cubic_interpolation(x):
	return 0.
#plotting

import matplotlib.pyplot as plt
plt.plot(xdata, ydata, 'o', xref, yref, '-')
plt.legend(['data', 'linear'], loc='best')
plt.show()
plt.savefig("interpolation.pdf", format="pdf")


#task 1.a):
print "Expected value of linear interpolation:"
print "x=0.4:",interpolate([0.4]).round(4)
print "x=-0.128:",interpolate([-0.128]).round(4)
print "x=-2.0:",interpolate([-2.0]).round(4)
print "x=3.2:",interpolate([3.2]).round(4)
"""
#task 1.b):
print "Expected value of cubic interpolation:"
print "x=0.4:",cubic_interpolation(0.4).round(4)
print "x=-0.128:",cubic_interpolation(-0.128).round(4)
print "x=-2.0:",cubic_interpolation(-2.0).round(4)
print "x=3.2:",cubic_interpolation(3.2).round(4)
"""

