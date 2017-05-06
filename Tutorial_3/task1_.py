import numpy as np
import matplotlib.pyplot as plt


data = open("data.txt", "r")
xdata=[]
ydata=[]
get_data = [line.strip().split() for line in data]
for i in range(len(get_data)):
	x = get_data[i][0]	
	y = get_data[i][1]
	xdata.append(x)
	ydata.append(y)

xdata=np.array(xdata)
ydata=np.array(ydata)


def interpolate(xdata,ydata,x):
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
