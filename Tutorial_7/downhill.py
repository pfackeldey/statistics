#!/usr/bin/python
import numpy as np

class DownhillSimplex():
    def __init__(self):
        self.function = function
        self.listoftuple = listoftuple
        self.alpha = alpha

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
        self.mid = [np.mean(self.values[:,i]) for i in range(1,self.values.shape[1])]
        return self.mid

    def reflection(self):
        r = [(1.+self.alpha)*self.mid[i]-self.alpha*self.values[-1,i+1] for i in range(len(self.mid))]
        return r

#Initialize required function, datapoints, parameters, ...:
def function(x,y):
    return (x**4. - 20.*x**2.)*np.exp(-y**2.) + (y**4. - 20.*y**2.)*np.exp(-x**2.) + 2.*(x**2. + y**2.) +10.*x + 5.*y + 200.
listoftuple = np.array([[0,0],[1,0],[1,1],[2,3],[3,4]])
alpha = 1.

#Initialize instance of Class DownhillSimplex:
downhill = DownhillSimplex()
print downhill.sort()
print downhill.midpoint()
print downhill.reflection()
