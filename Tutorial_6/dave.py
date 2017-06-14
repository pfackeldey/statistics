import numpy as np

def func2(x, param):
	f = 0.
	
	for i in xrange(len(param)):
		f += param[i]*x**i

	return f


def func(x,param):
	y=0.
	y=pow(x,4.)/300. + pow(x,3.)/50. -pow(x,2.)/3. +x/10. + 5./2.
	#~ return (x**4)/300. + (x**3)/50. - (x**2)/3. + x/10. +5./2.
	return y





	
def brent(func, param, a_ini, c_ini):

	root = 0.	
	accuracy = 10**(-5)
	missing_root = 1
	it = 0
	
	a = a_ini
	c = c_ini
	b = (a+c)/2.

	if(func(a, param)*func(c, param) > 0.):
		return False, it

	while(missing_root):

		R = func(b, param)/func(c, param)
		S = func(b, param)/func(a, param)
		T = func(a, param)/func(c, param)
		P = S*(T*(R-T)*(c-b)-(1.-R)*(b-a))
		Q = (T-1.)*(S-1.)*(R-1.)

		x_bs = (a+c)/2.
		x_qi = b + P/Q
		
		print "----------------------"	
		print "1",func(x_qi,param)
		print func2(x_qi,param)
		print "2",func(c,param)
		print func2(c,param)
		print "3",func(x_bs,param)
		print func2(x_bs,param)
		
		print "a,b",a,b
		
		if(abs(func(x_qi, param)) <= abs(func(x_bs, param))):
			if(func(x_qi, param)*func(c, param) > 0.):
				c = x_qi

			else:
				a = b
				b = x_qi


		
	
		else:
			if(func(x_bs, param)*func(c, param) > 0.):
				c = x_bs
	
			else:
				a = b
				b = x_bs


		print "4",func(b,param)
		print func2(b,param)

		if(abs(a-b)<=accuracy or abs(b-c)<=accuracy):
			#~ if(func(b, param)==0):
			if(func(b, param)<=accuracy):
				root = b
				missing_root = 0
		
			else:
				if(abs(a-b)<=accuracy):
					b = (b+c)/2.

				elif(abs(b==c)<=accuracy):
					b = (a+b)/2.
				

		else:
			if(abs(b-c) <= accuracy or abs(a-b) <= accuracy or abs(func(b,param)<=accuracy)):
				root = b
				missing_root = 0


		it+= 1

	return root, it	


def main():

	
	roots = []
	it = []
	coefficients = [5./2., 1./10., -1./3., 1./50., 1./300.]
	a = -20.
	b = 20.
	n = 20

	print "1",func(1.1111111111111111111,coefficients)
	print "2",func2(1.1111111111111111111,coefficients)

	ar=np.linspace(-100.,100.,1000000)

	#~ for i in ar:
		#~ if abs(func(i,coefficients)-func2(i,coefficients)):
			#~ print "error",i,func(i,coefficients),func2(i,coefficients)
			#~ print func(i,coefficients)-func2(i,coefficients)

	for i in xrange(n):
		root = brent(func, coefficients, a+i*(abs(b-a))/n, b - (n-1-i)*(abs(b-a))/n)

		if(root[0]):
			roots = np.append(roots, root[0])
			it = np.append(it, root[1])


	print "The polynomial function with the coefficients " + str(coefficients[::-1]) + " has the roots " + str(roots) + " after " + str(it) + " iterations."

	print brent(func, coefficients, -14., -11.)

main()
