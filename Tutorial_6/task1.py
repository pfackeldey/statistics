#!/usr/bin/python
import numpy as np


def bisection(x1,x2,cut):
    def func(x):
        return (x**4.)/300. + (x**3.)/50. - (x**2.)/3. + x/10. +5./2.
    i=0
    while i<=100:
        x = (x1+x2)/2.0
        if (func(x)==0 or abs(x1-x2)/2.0<=cut):
            break
        else:
            i=i+1
            if func(x)*func(x1)>0:
                x1 = x
            else:
                x2 = x
    return x

# all roots:

print "first root", bisection(-20.,-10.,0.00001)
print "second root", bisection(-5.,0.,0.00001)
print "third root", bisection(0.,5.,0.00001)
print "fourth root", bisection(5.,10.,0.00001)
