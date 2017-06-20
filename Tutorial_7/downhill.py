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
listoftuple =10. * np.random.rand(3,2) -5.
alpha = 1.
gamma = 2.
beta = 0.5
sigma = 0.5
#Initialize instance of Class DownhillSimplex:
downhill = DownhillSimplex()

values = downhill.sort()
mid = downhill.midpoint()
reflection = downhill.reflection()
expanded = downhill.expansion()
h = reflection if function(*reflection)<function(*values[-1][1:]) else values[-1][1:]
contracted = downhill.contraction(h)
print values

while(abs(function(*values[0][1:])-function(*values[1][1:]))>1e-5):
    if function(*reflection)<function(*values[0][1:]):
        values[-1][1] = expanded[0] if function(*expanded)<function(*mid) else reflection[0]
        values[-1][2] = expanded[1] if function(*expanded)<function(*mid) else reflection[1]
    elif function(*reflection)<function(*values[-2][1:]):
        values[-1][1] = reflection[0]
        values[-1][2] = reflection[1]
    else:
        values[-1][1] = contracted[0] if function(*contracted)<function(*values[-1][1:]) else values[-1][1]
        values[-1][2] = contracted[1] if function(*contracted)<function(*values[-1][1:]) else values[-1][2]
    for i in range(values.shape[0]):
        values[i][1] = sigma*values[0][1] + (1.-sigma)*values[i][1]
        values[i][2] = sigma*values[0][2] + (1.-sigma)*values[i][2]
    listoftuple = np.zeros((3,2))
    for i in range(listoftuple.shape[0]):
        listoftuple[i][0] = values[i][1]
        listoftuple[i][1] = values[i][2]
    downhill_update = DownhillSimplex()
    values = downhill_update.sort()
    mid = downhill_update.midpoint()
    reflection = downhill_update.reflection()
    expanded = downhill_update.expansion()
    h = reflection if function(*reflection)<function(*values[-1][1:]) else values[-1][1:]
    contracted = downhill_update.contraction(h)
    print values
