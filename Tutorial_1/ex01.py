#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Peter Fackeldey 330532
Sebastian Wuchterl 331453
"""


import argparse

parser = argparse.ArgumentParser(description='Comparing some functions :).')
parser.add_argument('--use-suitable', default=None,
                    help='Use suitable exponential function. Options: "None","time","accuracy". Default = None')
parser.add_argument('--variable', default=2.,
                    help='Set exponent of exponential function. Default = 2')
parser.add_argument('--computing-time', default=1.,
                    help='Set computing time for suitable exp function "time". Default = 1s')
parser.add_argument('--accuracy', default=1e-5,
                    help='Set accuracy for suitable exp function "accuracy". Default = 1e-5')

args = parser.parse_args()
import math

def exp(x):                         #exp.py
	result = 0
	step = 1.
	for n in range(1,51):
		result = result + step
		step = step*x/n
	print "With n = %d steps:"%n
	return result

def cos(x):
	result = 0.
	n= 1.
	step = 1.
	result_saved = 1.
	accuracy = float(args.accuracy)
	while (abs(result-result_saved) > accuracy):
		result_saved = result	
		result = result + step
		step = (-1.)**n * x**(2.*n) / math.factorial(2.*n) 
		n = n + 1	
	print "With n = %d steps:"%(n-1)
	return result

def sin(x):
	result = 0.
	n=0.
	step = 0.
	result_saved = 1.
	accuracy = float(args.accuracy)
	while (abs(result-result_saved) > accuracy):
		step = (-1.)**n * x**(2.*n+1) / math.factorial(2.*n+1) 		
		result_saved = result	
		result = result + step
		n = n + 1	
	print "With n = %d steps:"%(n-1)
	return result

def suitable_exp_time(x):
	import time
	result = 0
	n= 1
	step = 1
	time_end = time.time() + float(args.computing_time)
	while (time.time() < time_end):
		result = result + step
		step = step*x/n
		n = n + 1	
	print "With n = %d steps:"%n
	return result

def suitable_exp_accuracy(x):
	result = 0.
	n= 1
	step = 1
	result_saved = 1.
	accuracy = float(args.accuracy)
	while (abs(result-result_saved) > accuracy):
		result_saved = result	
		result = result + step
		step = step*x/n
		n = n + 1	
	print "With n = %d steps:"%n
	return result

def drawExp():
	import ROOT
	if args.use_suitable=="time":
		c1 = ROOT.TCanvas("c1","c1",800,800)
		f  = ROOT.TF1("suitable_exp_time","TMath::Exp(x)",0,2)
		f.Draw()
		c1.Print("suitable_exp_time_py.pdf")
	elif args.use_suitable=="accuracy":
		c1 = ROOT.TCanvas("c1","c1",800,800)
		f  = ROOT.TF1("suitable_exp_accuracy","TMath::Exp(x)",0,2)
		f.Draw()
		c1.Print("suitable_exp_accuracy_py.pdf")
	else: 
		c1 = ROOT.TCanvas("c1","c1",800,800)
		f  = ROOT.TF1("exp","TMath::Exp(x)",0,2)
		f.Draw()
		c1.Print("exp_py.pdf")
def main():
	x = float(args.variable)
	if args.use_suitable=="time":
		if x > 0:
			myexp = suitable_exp_time(x)
		else:
			myexp = 1./suitable_exp_time(-x)
		print "    my exp(x) = %.12f"%myexp
		print "python exp(x) = %.12f"%math.exp(x)
		drawExp()
	elif args.use_suitable=="accuracy":
		if x > 0:
			myexp = suitable_exp_accuracy(x)
		else:
			myexp = 1./suitable_exp_accuracy(-x)
		print "    my exp(x) = %.12f"%myexp
		print "python exp(x) = %.12f"%math.exp(x)
		drawExp()	
	else: 
		if x > 0:
			myexp = exp(x)
		else:
			myexp = 1./exp(-x)
		print "    my exp(x) = %.12f"%myexp
		print "python exp(x) = %.12f"%math.exp(x)
		drawExp()
	
	mycos = cos(x)
	print "    my cos(x) = %.12f"%mycos
	print "python cos(x) = %.12f"%math.cos(x)
	mysin = sin(x)
	print "    my sin(x) = %.12f"%mysin
	print "python sin(x) = %.12f"%math.sin(x)
main()

#########################################################################################
# execute script with '-h' option to view the command arguments for different functions.#
#########################################################################################

""" task a):
from lecture/ c-code:
With 50 steps
   my exp(x) = 23.1385440826
cmath exp(x) = 23.1385485756


result with code from tutorial-sheet:
With n = 50 steps:
    my exp(x) = 23.138548663861
python exp(x) = 23.138548663861

	
comparison: 
c code: abs(difference from true value)/true value -> 2*10^-7
python code: abs(difference from true value)/true value -> 0 
-->python more precise
"""

#task b):
"""
2 methods implemented, use --use-suitable -h

"""

# task c):
#Default accuracy = 1e-10: with command "python ex01.py --variable $exponent_value$ --use-suitable accuracy --accuracy 1e-10"
""" e^1:With n = 16 steps:
   	my exp(x) = 2.718281828458
	python exp(x) = 2.718281828459 

    e^2:With n = 20 steps:
    	my exp(x) = 7.389056098926
	python exp(x) = 7.389056098931

    e^4:With n = 27 steps:
   	my exp(x) = 54.598150033131
	python exp(x) = 54.598150033144

    e^8:With n = 40 steps:
    	my exp(x) = 2980.957987041717
	python exp(x) = 2980.957987041728

    e^16:With n = 61 steps:
    	my exp(x) = 8886110.520507872105
	python exp(x) = 8886110.520507872105
	
	
	increase in number of steps not linear, but increases with increasing exponent
	
"""

"""  task  d):
with command:
$ python ex01.py --variable 1.


With n = 6 steps:
    my cos(x) = 0.540302303792
python cos(x) = 0.540302305868
With n = 4 steps:
    my sin(x) = 0.841471009700
python sin(x) = 0.841470984808


comparison:
you get a result so accurate, as you set the accuracy parameter
default=1e-5

with a very high parameter, the value is equal to the true value

"""





