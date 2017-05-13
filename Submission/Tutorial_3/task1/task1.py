import numpy as np
from scipy import interpolate
from numpy.linalg import inv
import matplotlib.pyplot as plt

data = open("data.txt", "r")
get_data = [line.strip().split() for line in data]

xdata=np.array([])
ydata=np.array([])

for i in range(len(get_data)):
	x = get_data[i][0]	
	y = get_data[i][1]
	xdata=np.append(xdata,np.float(x))
	ydata=np.append(ydata,np.float(y))
data.close()




def interpolate(x):
	yref=np.array([])
	for entry in x:
		index1=0
		index2=0
		if(entry<=xdata[0]):
			index1=0
			index2=1
		if(entry>=xdata[len(xdata)-1]):
			index1=len(xdata)-2
			index2=len(xdata)-1
		for i in range(1,len(xdata)):
			if(entry>=xdata[i-1])and(entry<=xdata[i]):
				index1=i-1
				index2=i
		A=(xdata[index2]-entry)/(xdata[index2]-xdata[index1])
		B=1.-A
		y=A*ydata[index1]+B*ydata[index1+1]
		yref=np.append(yref,float(y))
	return yref



def cubic_interpolation(x):
	a=np.zeros(len(xdata)-1)
	b=np.zeros(len(xdata))
	c=np.zeros(len(xdata)-1)
	F=np.zeros(len(xdata))

	matrix=np.zeros((len(xdata),len(xdata)))

	for i in range(1,len(xdata)):
		a[i-1]=1./6.*(xdata[i]-xdata[i-1])
	for i in range(0,len(xdata)):
		if(i==0):
			b[i]=1.	#boundary condition
		else:
			if(i==len(xdata)-1):
				b[i]=1.
			else:
				b[i]=1./3. *(xdata[i+1]-xdata[i-1])
	for i in range(0,len(xdata)-1):
		c[i]=1./6. *(xdata[i+1]-xdata[i])
	for i in range(0,len(xdata)):
		if(i==0):
			F[i]=0.5	#boundary condition
		else:
			if(i==(len(xdata)-1)):
				F[i]=0.0	#boundary condition
			else:
				F[i]=(ydata[i+1]-ydata[i])/(xdata[i+1]-xdata[i]) - (ydata[i]-ydata[i-1])/(xdata[i]-xdata[i-1])
				
	for i in range(0,len(xdata)-1):
		matrix[i+1][i]=a[i]
		matrix[i][i]=b[i]
		matrix[i][i+1]=c[i]
	matrix[len(xdata)-1][len(xdata)-1]=b[len(xdata)-1]
	
	F.transpose()
	Minv=inv(matrix) 
			
	y2derivative=np.zeros(len(xdata))
	y2derivative=np.dot(Minv,F)

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
		A=(xdata[index2]-entry)/(xdata[index2]-xdata[index1])
		B=1.-A
		C=1./6.*(A**3. - A)*(xdata[index2]-xdata[index1])**2.
		D=1./6.*(B**3. - B)*(xdata[index2]-xdata[index1])**2.
		y=A*ydata[index1]+B*ydata[index1+1]	+C*y2derivative[index1] +D*y2derivative[index1+1]
		yref=np.append(yref,float(y))
	return yref
	
	
#for plotting
x2plot=np.arange(-2.25,4.05,0.05)#data for grid to plot
y2plot=interpolate(x2plot)
y2plot_cubic=cubic_interpolation(x2plot)

#plotting


plt.plot(xdata, ydata, 'o', x2plot, y2plot, '-')
plt.plot( x2plot, y2plot_cubic, '-')
plt.legend(['data', 'linear','cubic'], loc='best')
plt.savefig("interpolation.png", format="png")
plt.show()



#task 1.a):
print "Expected value of linear interpolation:"
print "x=0.4:",interpolate([0.4]).round(4)
print "x=-0.128:",interpolate([-0.128]).round(4)
print "x=-2.0:",interpolate([-2.0]).round(4)
print "x=3.2:",interpolate([3.2]).round(4)

#task 1.b):
print "Expected value of cubic interpolation:"
print "x=0.4:",cubic_interpolation([0.4]).round(4)
print "x=-0.128:",cubic_interpolation([-0.128]).round(4)
print "x=-2.0:",cubic_interpolation([-2.0]).round(4)
print "x=3.2:",cubic_interpolation([3.2]).round(4)

#task 1.d):
"""
While playing with the boundary conditions one obtains that especially the boundary condition of the last entry of the F array changes a lot in performance. The last two points have a slope near to 0, which does not allow big numbers for this boundary condition. Otherwise you will get huge oszillations in the last few x-values! 
best boundary conditions found: b[0]=1., F[0]=0.5 and F[last_index]=0.0
"""

#task 1.e):
"""
The best solution gives the cubic spline interpolation, but only if you find the right boundary conditions. Otherwise you will get huge oszillations and the prediction of the interpolation rountine will get really bad. This routine allows way better prediction of the solution because you take higher order of the polynomial taylor expansion.  
"""

