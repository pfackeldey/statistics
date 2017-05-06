import numpy as np
from scipy.interpolate import interp1d

#open data
data = open("data.txt", "r")

#read data and save it in np arrays
get_data = [line.strip().split() for line in data]

print get_data

xdata=[]
ydata=[]

for i in range(len(get_data)):
	x = get_data[i][0]	
	y = get_data[i][1]
	xdata.append(x)
	ydata.append(y)
print xdata
print ydata

#change datatype of xdata array:
xdata = map(np.float64, xdata)

#linear interpolation
linear_interpolation = interp1d(xdata,ydata)

#cubic interpolation
cubic_interpolation = interp1d(xdata,ydata, kind="cubic")


#plotting
import matplotlib.pyplot as plt
plt.plot(xdata, ydata, 'o', xdata, linear_interpolation(xdata), '-',xdata, cubic_interpolation(xdata), '--')
plt.legend(['data', 'linear','cubic'], loc='best')
plt.show()

#task 1.a):
print "Expected value of linear interpolation:"
print "x=0.4:",linear_interpolation(0.4).round(4)
print "x=-0.128:",linear_interpolation(-0.128).round(4)
print "x=-2.0:",linear_interpolation(-2.0).round(4)
print "x=3.2:",linear_interpolation(3.2).round(4)

#task 1.b):
print "Expected value of cubic interpolation:"
print "x=0.4:",cubic_interpolation(0.4).round(4)
print "x=-0.128:",cubic_interpolation(-0.128).round(4)
print "x=-2.0:",cubic_interpolation(-2.0).round(4)
print "x=3.2:",cubic_interpolation(3.2).round(4)

data.close()
