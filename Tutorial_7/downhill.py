#!/usr/bin/python
import numpy as np

def function(x,y):
    return (x**4. - 20.*x**2.)*np.exp(-y**2.) + (y**4. - 20.*y**2.)*np.exp(-x**2.) + 2.*(x**2. + y**2.) +10.*x + 5.*y + 200.


listoftuple=np.array([[0,0],[1,0],[1,1],[2,3],[3,4]])

def sort(function, x):
    values=np.zeros((x.shape[0],x.shape[1]+1))
    for tuples,i in zip(x,range(len(x))):
        values[i][0]=function(*tuples)
        for j in range(x.shape[1]):
            values[i][j+1]=tuples[j]
    values = values[values[:,0].argsort()]
    return values

print sort(function,listoftuple)

def midpoint(values):
    values = values[:values.shape[0]-1,:]
    midpoint = [np.mean(values[:,i]) for i in range(1,values.shape[1])]
    return midpoint

print midpoint(sort(function,listoftuple))
