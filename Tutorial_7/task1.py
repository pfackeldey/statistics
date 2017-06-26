#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
n=2   # dimensions

# define class with all necessary functions
class DownhillSimplex():
    def __init__(self):
        self.function = function
        self.listoftuple = listoftuple
        self.alpha = alpha
        self.gamma = gamma
        self.beta = beta

    def sort(self):
        values=np.zeros((self.listoftuple.shape[0],self.listoftuple.shape[1]+1))
        for tuples,i in zip(self.listoftuple,range(len(self.listoftuple))):
            values[i][0]=self.function(*tuples)
            for j in range(self.listoftuple.shape[1]):
                values[i][j+1]=tuples[j]
        self.values = values[values[:,0].argsort()]
        return self.values

    def midpoint(self):
        self.values = self.values[:self.values.shape[0]-1,:]
        self.mid = [np.mean(self.values[:-1,i]) for i in range(1,self.values.shape[1])]
        return self.mid

    def reflection(self):
        r = [(1.+self.alpha)*self.mid[i]-self.alpha*self.values[-1,i+1] for i in range(len(self.mid))]
        return r

    def expansion(self):
        e = [(1.+self.gamma)*self.mid[i]-self.gamma*self.values[-1,i+1] for i in range(len(self.mid))]
        return e

    def contraction(self, h):
        c = [self.beta*self.mid[i]+(1.-self.beta)*h[i] for i in range(len(self.mid))]
        return c




#Initialize required function, datapoints, parameters, ...:
def function(x,y):
    return (x**4. - 20.*x**2.)*np.exp(-y**2.) + (y**4. - 20.*y**2.)*np.exp(-x**2.) + 2.*(x**2. + y**2.) +10.*x + 5.*y + 200.
    
arr=[]
for test in range(1):   #change here number for more than 1 run / in plot are 3000 runs
    print test # print current run for verbose
    listoftuple =8. * np.random.rand(3,2) -4.   # generate 3 random points for corners of simplex
    alpha = 1.  # define paramaters for reflection and so on
    gamma = 2.
    beta = 0.5
    sigma = 0.5
    #Initialize instance of Class DownhillSimplex:
    downhill = DownhillSimplex()
    values = downhill.sort()
    j=0
    while(j<100):   # no convergence criteria / set iterations to 100
        j=j+1
        values = downhill.sort()
        mid = downhill.midpoint()
        reflection = downhill.reflection()
        expanded = downhill.expansion()
        h = reflection if function(*reflection)<function(*values[-1][1:]) else values[-1][1:]
        contracted = downhill.contraction(h)
        if function(*reflection)<function(*values[0][1:]):    # if reflected is better, take that one
            values[-1][1] = expanded[0] if function(*expanded)<function(*reflection) else reflection[0]
            values[-1][2] = expanded[1] if function(*expanded)<function(*reflection) else reflection[1]
            listoftuple = np.zeros((3,2))
            for i in range(listoftuple.shape[0]):
                listoftuple[i][0] = values[i][1]
                listoftuple[i][1] = values[i][2]
            downhill = DownhillSimplex()
            continue
        elif function(*reflection)<function(*values[-2][1:]):   # else test if reflected is better than x_n-1
            values[-1][1] = reflection[0]
            values[-1][2] = reflection[1]
            listoftuple = np.zeros((3,2))
            for i in range(listoftuple.shape[0]):
                listoftuple[i][0] = values[i][1]
                listoftuple[i][1] = values[i][2]
            downhill = DownhillSimplex()
            continue
        elif function(*contracted)<function(*values[-1][1:]): # else try contraction and test again
            values[-1][1] = contracted[0]
            values[-1][2] = contracted[1]
            listoftuple = np.zeros((3,2))
            for i in range(listoftuple.shape[0]):
                listoftuple[i][0] = values[i][1]
                listoftuple[i][1] = values[i][2]
            downhill = DownhillSimplex()
            continue
        else:   # else shrink hole simplex
            for i in range(values.shape[0]):
                values[i][1] = sigma*values[0][1] + (1.-sigma)*values[i][1]
                values[i][2] = sigma*values[0][2] + (1.-sigma)*values[i][2]
            listoftuple = np.zeros((3,2))
            for i in range(listoftuple.shape[0]):
                listoftuple[i][0] = values[i][1]
                listoftuple[i][1] = values[i][2]
            downhill = DownhillSimplex()
            continue
    print values[0] # print final result for minima (f,x,y)
    arr.append(values)

# plotting part / uncomment if you want to make the histogram
"""
arr=np.array(arr)
xses=arr[:,0,1]
yses=arr[:,0,2]
fig, ax = plt.subplots()
h = ax.hist2d(xses, yses, bins=60,range=[[-4., 4.], [-4., 4.]])
plt.colorbar(h[3], ax=ax)
plt.show()
"""


# following code was for testing, where the minimas are

"""
from scipy.optimize import fmin
def function(t):
    x,y=t
    return (x**4. - 20.*x**2.)*np.exp(-y**2.) + (y**4. - 20.*y**2.)*np.exp(-x**2.) + 2.*(x**2. + y**2.) +10.*x + 5.*y + 200.
    
mini=[]
for i in range(100):
    mini.append(fmin(function,[i,i],full_output=1)[0])
    print fmin(function,[i,i],full_output=1)
mini=np.array(mini)
print mini[:,1]

"""






