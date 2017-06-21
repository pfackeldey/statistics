# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:32:03 2017

@author: Sebastian
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def func(x,y):
    sigma_x1=1.5
    sigma_y1=1.    
    sigma_x2=1.5
    sigma_y2=1.
    mu_x1=1.
    mu_x2=1.
    mu_y1=-1.
    mu_y2=2.
    sigma_xy1=0.9
    sigma_xy2=0.4
    gauss_2D_1 = mlab.bivariate_normal(x, y, sigma_x1, sigma_y1, mu_x1, mu_y1, sigma_xy1)
    gauss_2D_2 = mlab.bivariate_normal(x, y, sigma_x2, sigma_y2, mu_x2, mu_y2,sigma_xy2)
    return 0.4*gauss_2D_1+25.*gauss_2D_2/(0.4+25.)
 
    
N=1000
x_ini = np.zeros(2)
p_ini = func(x_ini[0], x_ini[1])
data=[]

x=x_ini
p=p_ini

for i in range(N):
    x_new = x + np.random.normal(size=2)
    p_new = func(x_new[0], x_new[1])
    a=min(1.,p_new/p)  
    if a >= 1.:
        x = x_new
        p = p_new
    else:
        P = np.random.rand()
        if P < a:
            x = x_new
            p = p_new
    data.append(x)
    


data = np.array(data)
plt.scatter(data[:, 0], data[:, 1], alpha=0.5, s=1)
dx = 0.01
x = np.arange(np.min(data), np.max(data), dx)
y = np.arange(np.min(data), np.max(data), dx)
X, Y = np.meshgrid(x, y)
Z = func(X, Y)
CS = plt.contour(X, Y, Z, 10)
plt.clabel(CS, inline=1, fontsize=10)
plt.show()    