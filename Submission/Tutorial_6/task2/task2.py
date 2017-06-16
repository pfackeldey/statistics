import numpy as np
import matplotlib.pyplot as plt

def func(x):
	return (x**4.)/300. + (x**3.)/50. - (x**2.)/3. + x/10. +5./2.
	
	
def brent(f,start_point,end_point,accuracy):
	
	acc=accuracy
	
	a=start_point
	b=end_point
	
	f_a=f(a)
	f_b=f(b)
	
	if(f_a*f_b > 0.):
		#~ print "no roots in given interval found"
		return False,0
	
	c=a
	f_c=f_a
	
	d=b-a
	e=d
	
	count=0
	max_steps=1000
	
	while (count<max_steps):
		count+=1
		
		if (f_b*f_c>0.):
			c=a
			f_c=f_a
			d=b-a
			e=d
			
		if (abs(f_c)<abs(f_b)):
			a=b
			b=c
			c=a
			f_a=f_b
			f_b=f_c
			f_c=f_a
			
		tol=2.*abs(b)*acc
		m=(c-b)/2.
		
		if(abs(m)>tol) and (abs(f_b)>0.):
			
			if(abs(e)<tol) or (abs(f_a) <= abs(f_b)):
				d=m
				e=m
			else:
				S=f_b/f_a
				if (a==c):
					P=2.*m*S
					Q=1.-S
				else:
					Q=f_a/f_c
					R=f_b/f_c
					P=S*(2.*m*Q*(Q-R)-(b-a)*(R-1.))
					Q=(Q-1.)*(R-1.)*(S-1.)
				if (P>0.):
					Q=-Q
				else:
					P=-P
					
				S=e
				e=d
				
				if (2.*P < 3.*m*Q-abs(tol*Q)) and (P < abs(S*Q/2.)):
					d=P/Q
				else:
					d=m
					e=m
					
			a=b
			f_a=f_b
			
			if (abs(d)>tol):
				b=b+d
			else:
				if (m>0.):
					b=b+tol
				else:
					b=b-tol
				
		else:
			break
		f_b=f(b)
		
	return b,count






def rootfinding(function):

	acc=np.finfo(float).eps

	start_guess=-30.
	end_guess=30.
	N=30

	roots=[]
	its=[]

	for i in xrange(N):
			width=abs(start_guess-end_guess)
			start=start_guess+i*width/N
			end=end_guess- (N-1-i)*width/N
			root,iterations = brent(function, start, end,acc)
			if (root):
				roots.append(root)
				its.append(iterations)
				
	return roots,its


roots,iterations=rootfinding(func)
roots=np.array(roots)
for i in range(len(roots)):
	print "root found at x= "+str(roots[i])+" with "+str(iterations[i])+" iterations"
plt.figure()
x=np.linspace(-15.,15.,10000.)
y=func(x)
plt.plot(x,y,label="function")
plt.plot(roots,np.zeros(len(roots)),"o",label="roots")
plt.legend(loc="best")
plt.grid()
plt.show()









