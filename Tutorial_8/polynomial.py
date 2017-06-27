#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats as st

data = np.loadtxt("data.dat", skiprows=1)

x_data = data[:,0]
y_data = data[:,1]
y_err = data[:,2]

def polynomial3(x,a,b,c,d):
    return a+b*x+c*x**2.+d*x**3.


popt, pcov = curve_fit(polynomial3, x_data, y_data)

def chi2(y_exp,y_obs,y_err):
    return sum(((y_obs-y_exp)**2.)/(y_err**2.))

print "chi2: ", chi2(y_data, polynomial3(x_data, *popt), y_err)
print "chi2/dof: ", chi2(y_data, polynomial3(x_data, *popt), y_err)/(len(y_data)-4.)


plt.errorbar(x_data,y_data,yerr=y_err, label='data')
plt.plot(x_data, polynomial3(x_data, *popt), 'r-', label='fit')
plt.text(14, 140, "chi2/dof: "+str(chi2(y_data, polynomial3(x_data, *popt), y_err)/(len(y_data)-4.)))
plt.legend()
plt.show()
plt.close()

#Wald-Wolfowitz
R=[]

for entry,i in zip(x_data,range(len(x_data))):
    if (polynomial3(entry, *popt)-y_data[i]>0):
        R.append('A')
    else:
        R.append('B')

print "Run result: ", R

#number of runs:
r=1.

for i in range(1,len(R)):
    if R[i]!=R[i-1]:
        r+=1.
    else:
        pass

r_mean = 1.+(2.*R.count("A")*R.count("B"))/len(R)
r_var = (2.*R.count("A")*R.count("B")*(2.*R.count("A")*R.count("B")-len(R)))/(len(R)**2. *(len(R)-1))
Z=(r-r_mean)/np.sqrt(r_var)
p=1.-st.norm.pdf(Z)
print "runs: ", r

print "N_A: ", R.count("A")
print "N_B: ", R.count("B")
print
print "expected <r>: ", r_mean
print
print "variance r: ", r_var
print
print "Z-Score of r: ", Z
print
print "p-value: ", p
