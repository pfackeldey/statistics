import numpy as np
import matplotlib.pyplot as plt

def func(x):
	return (x**4.)/300. + (x**3.)/50. - (x**2.)/3. + x/10. +5./2.


def bisection(func,x1,x2,cut):
    i=0
    
    if(func(x1)*func(x2) > 0.):
		#~ print "no roots in given interval found"
		return False,0
    
    while i<1000:
        x = (x1+x2)/2.
        i+=1
        if (abs(func(x))<=cut or abs(x1-x2)/2.<=cut):
            break
        else:
            #~ i=i+1
            if func(x)*func(x1)>0.:
                x1 = x
            else:
                x2 = x
    return x,i

# all roots:

#~ print "first root", bisection(-20.,-10.,0.00001)
#~ print "second root", bisection(-5.,0.,0.00001)
#~ print "third root", bisection(0.,5.,0.00001)
#~ print "fourth root", bisection(5.,10.,0.00001)




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
			root,iterations = bisection(function, start, end,acc)
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
