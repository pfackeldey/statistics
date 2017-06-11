#!/usr/bin/python
import numpy as np


def bisection(x1,x2,cut):
    def func(x):
        return (x**4.)/300. + (x**3.)/50. - (x**2.)/3. + x/10. +5./2.
    i=0
    while i<=100:
        x = (x1+x2)/2.0
        print "x1="+str(x1)+" ; x2="+str(x2)+" ; x="+str(x)+" ; f(x)="+str(func(x))
        if (func(x)==0 or abs(x1-x2)/2.0<=cut):
            break
        else:
            i=i+1
            if func(x)*func(x1)>0:
                x1 = x
            else:
                x2 = x
    return x


print bisection(0.,4.,0.00001)
