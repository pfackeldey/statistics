import numpy as np

def func(x):
	return (x**4.)/300. + (x**3.)/50. - (x**2.)/3. + x/10. +5./2.

def brent(f,start,end,accuracy):

	root=0.
	count=0.

	a=start
	c=end
	b=(a+b)/2.


	if(f(a)*f(c)>0.):
		print "no roots found"
		break
		return False,False


	while ((abs(b-a)<accuracy)or(abs(b-c)<accuracy)):

		R=f(b)/f(c)
		S= f(b)/f(a)
		T=f(a)/f(c)

		P=S*(T*(R-T)*(c-b)-(1-R)*(b-a))
		Q=(T-1)*(R-1)*(S-1)

		x_quadr=b+P/Q


		if not((S==1.)or(T==1.)or(R==1.)):
			if(f(x_quadr)*f(c)>0.):
				c=x_quadr
			else:
				a=b
				b=x_quadr

		else:
			if(a==b):
				x_bisection=(a+c)/2.
			elif(a==c):
				x_bisection=(a+b)/2.
			else:
				x_bisection=(b+c)/2.

			if(f(x_bisection)*f(c)>0.):
				a=b
				b=x_bisection

		count+=1.
	root=b
	return root,count
