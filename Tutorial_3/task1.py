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
	xdata=np.append(xdata,float(x))
	ydata=np.append(ydata,float(y))
print xdata
print ydata
data.close()

#linear interpolation
def interpolate(x):
	index1=0
	index2=0
	if(x<xdata[0]):
		index1=0
		index2=1
	if(x>xdata[len(xdata)-1]):
		index1=len(xdata)-2
		index2=len(xdata)-1
	for i in range(1,len(xdata)-1):
		if(x>xdata[i-1])and(x<xdata[i]):
			index1=i-1
			index2=i
	
	slope=(ydata[index2]-ydata[index1])/(xdata[index2]-xdata[index1])
	b=ydata[index1]-slope*xdata[index1]
	
	return slope*x+b

linear_interpolation = interpolate(0.4)
xref=np.arange(-2.1,3.8,0.1)
print xref



#cubic interpolation



#plotting

import matplotlib.pyplot as plt
plt.plot(xdata, ydata, 'o', xref, linear_interpolation(xref), '-')
plt.legend(['data', 'linear'], loc='best')
plt.show()


#task 1.a):
print "Expected value of linear interpolation:"
print "x=0.4:",linear_interpolation(0.4).round(4)
print "x=-0.128:",linear_interpolation(-0.128).round(4)
print "x=-2.0:",linear_interpolation(-2.0).round(4)
print "x=3.2:",linear_interpolation(3.2).round(4)
"""
#task 1.b):
print "Expected value of cubic interpolation:"
print "x=0.4:",cubic_interpolation(0.4).round(4)
print "x=-0.128:",cubic_interpolation(-0.128).round(4)
print "x=-2.0:",cubic_interpolation(-2.0).round(4)
print "x=3.2:",cubic_interpolation(3.2).round(4)
"""

