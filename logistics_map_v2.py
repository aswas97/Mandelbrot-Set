# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:52:49 2019

@author: 09oli
"""
import matplotlib.pyplot as plt
import numpy
iterations = 20000
a = 0.5
r = int(2)
points=[]

for n in range(3):
    r = int(2)
    a = 0.5
    while (r < 4):
        for i in range(iterations - n):
            a = a*r*(1 - a)
        points.append(a)
        r = r + 0.0001

x_values = numpy.arange(2, 4, 0.0001)
x_values_list = list(x_values)
x_values_list = x_values_list * 3
plt.scatter(x_values_list, points, s = 0.1) 
plt.xlabel('r', fontsize=18)
plt.ylabel('x', fontsize=16) 

plt.show()

