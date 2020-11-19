# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:02:08 2020

@author: Sohail Dua
"""

import numpy as np
import matplotlib.pyplot as plt

#n= int(input("Enter the no of elements"))
#arr = np.array([[int(x) for x in input(f"Enter the value{[i]}:").split()] for i in range(n)])

arr = np.array([[1,5], [2, 3] ,[4 ,1] ,[8, 1],[1,5], [2, 32] ,[41 ,14] ,[81, 5]])

print(arr)

x = arr[:,0]
#Separate x and y values

y = arr[:,1]


coefficients = np.polyfit(x, y, 8)


poly = np.poly1d(coefficients)
print(poly)


new_x = np.linspace(x[0], x[-1])


new_y = poly(new_x)


plt.plot(x, y, "o", new_x, new_y)


plt.xlim([x[0]-1, x[-1] + 1 ])

plt.savefig("line.jpg")