import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def quadratic(x):
	return x**2.
	
	
def linear(x):
	return x
	
x_data=[1.,2.,3.,4.,5.]
x_data =np.array(x_data)
#~ y_data = quadratic(x_data)

start=1.
end=5.
steps=5.

def trapezoidal(a,b,func,n):
	intervals=n-1
	h= (b-a)/intervals
	value=(func(a)+func(b))
	for i in range(1,intervals):
		value=value+2.*func(a+i*h)
	value=h*0.5 *value
	return value
	
def simpson(a,b,func,n):
	intervals=n-1
	h= (b-a)/intervals
	value=(func(a)+func(b))
	for i in range(1,intervals):
		if ((i%2)==0):
			c=2.
		else:
			c=4.
		value=value+c*func(a+i*h)
	value=h / 3. *value
	return value


print "int x from 1 to 5"
print "true value:", integrate.quad(linear, 1.,5.)[0]
print "trapezoidal", trapezoidal(1.,5.,linear,5)
print "difference" , abs(integrate.quad(linear, 1.,5.)[0]-trapezoidal(1.,5.,linear,5))
print "difference" , abs(integrate.quad(linear, 1.,5.)[0]-simpson(1.,5.,linear,5))

print "simpson", simpson(1.,5.,linear,5)
print ""
print "int x^2 from 1 to 5"
print "true value:", integrate.quad(quadratic, 1.,5.)[0]
print "trapezoidal", trapezoidal(1.,5.,quadratic,5)
print "difference" , abs(integrate.quad(quadratic, 1.,5.)[0]-trapezoidal(1.,5.,quadratic,5))
print "simpson", simpson(1.,5.,quadratic,5)
print "difference" , abs(integrate.quad(quadratic, 1.,5.)[0]-simpson(1.,5.,quadratic,5))













#~ plt.figure(0)
#~ plt.plot(x_data,y_data,'.')
#~ plt.show()
