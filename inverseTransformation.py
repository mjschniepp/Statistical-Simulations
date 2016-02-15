'''
    Implementation of the Inverse Transformation Method of R.V. Sampling
    Author: Michael Schniepp
'''

import numpy as np
import matplotlib.pyplot as plt

def Finv(x):                  # this is the CDF in which we are sampling
    y = np.sqrt(x/float(1-x))
    return y
    
n = 1000
rvList = []

for i in range(0,n):
    U = np.random.uniform(0,1)
    X = Finv(U)
    rvList.append(X)
    
print(np.mean(rvList))

# Plot of the pdf f(x) for comparison
def pdf(x):
    y = 2*x / float((1+x**2)**2)
    return y
    
test = []
dom = np.arange(0,20,0.1)
for i in dom:
    test.append(pdf(i))
    
    
# plot comparison of distribution of samples vs the pdf
f, axarr = plt.subplots(2, sharex=True)
axarr[0].set_title('Sampling Distribution')
axarr[0].hist(rvList, bins = 60)
axarr[1].set_title('f(x)')
axarr[1].plot(dom,test)
plt.show()