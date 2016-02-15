'''
    A Non-Homogenous Poisson Prcoess {N(t);t>=0}
    With intensity function: lambda(t) = 2t +2
    We then estimate the expected value of the first event time
'''

import numpy as np
import matplotlib.pyplot as plt


def test_density(x):
    y = ((2*x + 2)*np.exp(x-x*(2*x+2)))/float(3)
    return y
    
rvStorage = []

while len(rvStorage) < 1000:
    Y = np.random.exponential(1)
    U = np.random.uniform(0,1)
    if U <= test_density(Y):
        rvStorage.append(Y)
        
mu = np.mean(rvStorage)
def var(data):
    for i in range(0,len(data)):
        data[i] = (data[i] - mu)**2
    var = sum(data)/float(len(data))
    return var
    

print 'Expected Value', mu
print 'Theoretical E(X)', 1/float(4)
print 'Variance', var(rvStorage)
print 'Theoretical', 1/float(16)
        
# plot comparison of distribution of samples vs the pdf
def pdf(t):
    y = (2*t+2)*np.exp(-(2*t+2)*t)
    return y

test = []
dom = np.arange(0,1.5,0.1)
for i in dom:
    test.append(pdf(i))


f, axarr = plt.subplots(2, sharex=True)
axarr[0].set_title('Sampling Distribution')
axarr[0].hist(rvStorage, bins = 40)
axarr[1].set_title('f(x)')
axarr[1].plot(dom,test)
plt.show()        
