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


#plotting
import matplotlib.pyplot as plt
plt.plot(xdata, ydata, 'o', xdata, linear_interpolation(xdata), '-')
plt.legend(['data', 'linear'], loc='best')
plt.show()

#task 1.a):
print 

data.close()
