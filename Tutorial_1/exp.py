def exp(x):                         #exp.py
	result = 0
	step = 1.
	for n in range(1,51):
		result = result + step
		step = step*x/n
	print "With n = %d steps:"%n
	return result
	
import time
	
	
	
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
	
	
def cos(x):
	result=0.
	step=1.
	accuracy=0.000000000001
	result_save=1.
	n=1.
	while(abs(result-result_save)>accuracy):
		result_save=result
		result=result+step
		step=(-1.)**n * x**(2.*n)/(factorial(2*n))
		n=n+1
	print "With n = %d steps:"%(n-1)
	return result
	
	
	
def sin(x):
	result=0.
	step=1.
	accuracy=0.000000000001
	result_save=1.
	n=1.
	while(abs(result-result_save)>accuracy):
		result_save=result
		result=result+step
		step=(-1.)**n * x**(2.*n+1.)/(factorial(2*n+1.))
		n=n+1
	print "With n = %d steps:"%(n-1)
	return result		
	
def more_suitable_exp(x):
	result=0.
	step= 1
	result_save=1.
	accuracy=0.000000000001
	n=1
	time_end=time.time()+0.1*1
	while (time.time()<time_end):
		while (abs(result-result_save)>accuracy):
			result_save=result
			result = result + step
			step = step*x/n	
			n=n+1
	print "With n = %d steps:"%(n-1)	
	return result	
	
def drawExp():
	import ROOT
	c1 = ROOT.TCanvas("c1","c1",800,800)
	f  = ROOT.TF1("exp","TMath::Exp(x)",0,2)
	f.Draw()
	c1.Print("exp_py.pdf")
	
def main():
	from sys import argv
	import math
	x = float(argv[1])
	if x > 0:
		myexp = exp(x)
		#~ myexp = more_suitable_exp(x)
	else:
		myexp = 1./more_suitable_exp(-x)
	print "    my exp(x) = %.12f"%myexp
	print "python exp(x) = %.12f"%math.exp(x)
	print "    my cos(x) = %.12f"%cos(x)
	print "python cos(x) = %.12f"%math.cos(x)
	print "    my sin(x) = %.12f"%sin(x)
	print "python sin(x) = %.12f"%math.sin(x)
	drawExp()
	
	
main()



"""
1a)
from lecture/ c-code:
	With 50 steps
	   my exp(x) = 23.1385440826
	cmath exp(x) = 23.1385485756

result with code above:
	With 50 steps
	my exp(x) = 23.1385440826
	cmath exp(x) = 23.1385485756	
--> python version more precise, similar to cmath result 
1c)
1:With n = 16 steps:
    my exp(x) = 2.718281828459
python exp(x) = 2.718281828459
2:With n = 21 steps:
    my exp(x) = 7.389056098931
python exp(x) = 7.389056098931
4: With n = 29 steps:
    my exp(x) = 54.598150033144
python exp(x) = 54.598150033144
8: With n = 42 steps:
    my exp(x) = 2980.957987041728
python exp(x) = 2980.957987041728
16: With n = 60 steps:
    my exp(x) = 8886110.520507872105
python exp(x) = 8886110.520507872105








"""
