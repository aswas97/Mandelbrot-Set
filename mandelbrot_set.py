# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:40:57 2018

@author: sma18ob
"""
import numpy
import matplotlib.pyplot as plt

def mandelbrot(Re, Im, iterations):
    c = complex(Re, Im)
    z = 0.0j
    # this for loop checks number of iterations for the sequence to be >= 4
    for i in range(iterations):
        z = z**2 + c
        if z.real**2 + z.imag**2 >=4:
            return i
    return iterations

rows = 2000
columns = 3000
result = numpy.zeros([rows, columns])  #numpy grid is specified as 2000 by 3000 rectangle

for row_index, Re in enumerate(numpy.linspace(-2, 1, rows)): #iterates through each row
    for column_index, Im in enumerate(numpy.linspace(1, -1, columns)): #iterates through each column
        result[row_index, column_index] = mandelbrot(Re, Im, 100)  #each point is used to check iterations and then assigned to that block

#imshow allows for heat maps tpo be produced easily
plt.imshow(result.T, cmap="hot", extent=[-2, 1, -1, 1])#result.T reverses the image
plt.xlabel("Re") #lables axis
plt.ylabel("Im")
plt.show