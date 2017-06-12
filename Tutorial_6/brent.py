import numpy as np

def func(x):
	return (x**4.)/300. + (x**3.)/50. - (x**2.)/3. + x/10. +5./2.
	
def brent(f,start,end,accuracy):
	
	root=0.
	count=0.
	
	a=start
	c=end
	b=(a+c)/2.
	status=True
	
	if(f(a)*f(c)>0.):
		print "no roots found"
		return False,False
	
	while (status):
		
		count+=1.
	return root,count


acc=0.00001
print brent(func,-14.,-11	.,acc)



