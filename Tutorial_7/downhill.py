#!/usr/bin/python
import numpy as np

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
        self.mid = [np.mean(self.values[:,i]) for i in range(1,self.values.shape[1])]
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
listoftuple = np.random.rand(10,2)
alpha = 1.
gamma = 2.
beta = 0.5
sigma = 0.5
#Initialize instance of Class DownhillSimplex:
downhill = DownhillSimplex()
print downhill.sort()
print downhill.midpoint()
print downhill.reflection()
print downhill.expansion()

values = downhill.sort()
print values[-1]
print values[0][1]
print values[0][2]
print values.shape[0]

i=0

while(i<3):
    mid = downhill.midpoint()
    values = downhill.sort()
    if function(*mid)<function(*values[0][1:]):
        expanded = downhill.expansion()
        values[-1][1] = expanded[0] if function(*expanded)<function(*mid) else mid[0]
        values[-1][2] = expanded[1] if function(*expanded)<function(*mid) else mid[1]
    elif function(*mid)<function(*values[-2][1:]):
        values[-1][1] = mid[0]
        values[-1][2] = mid[1]
    else:
        h = mid if function(*mid)<function(*values[-1][1:]) else values[-1][1:]
        contracted = downhill.contraction(h)
        values[-1][1] = contracted[0] if function(*contracted)<function(*values[-1][1:]) else values[-1][1]
        values[-1][2] = contracted[1] if function(*contracted)<function(*values[-1][1:]) else values[-1][2]
    for i in range(values.shape[0]):
        values[i][1] = sigma*values[0][1] + (1.-sigma)*values[i][1]
        values[i][2] = sigma*values[0][2] + (1.-sigma)*values[i][2]
    i=i+1
    print values
