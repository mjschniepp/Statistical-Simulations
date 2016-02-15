'''
Testing for a Monte Carlo Method to approximate Pi
'''

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    r = x**2 + y**2
    return r

n = 100000
inx_coords = []
iny_coords = []
outx_coords = []
outy_coords = []
for i in range(0,n):
    X = np.random.uniform(-1,1)
    Y = np.random.uniform(-1,1)
    if f(X,Y) <= 1:
        inx_coords.append(X)
        iny_coords.append(Y)
    else:
        outx_coords.append(X)
        outy_coords.append(Y)
    
appx = len(inx_coords)/float(n)
print(4*appx)

plt.plot(inx_coords, iny_coords,'ro',outx_coords,outy_coords,'bo')
plt.show()