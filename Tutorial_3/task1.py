import numpy as np

data = open("data.txt", "r")

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

data.close()
