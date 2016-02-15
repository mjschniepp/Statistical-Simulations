'''
    Inhomogeneous Poisson Process via Homogeneous Poisson Process
    Method of Thinning
'''
import numpy as np
import matplotlib.pyplot as plt

def l(t):           # intensity function
    y = 2.*t + 2.
    return y

firstEvents = []
T = 15.
L = l(T)
events = np.random.poisson(T*L)

Vtimes = []
Utimes = []
numEvents = []
for i in range(0,events):
    Vtimes.append(np.random.uniform(0,T))

for i in range(0,events):
    Utimes.append(np.random.uniform(0,1))

sUtimes = sorted(Utimes)
nhpp = []

for i,j in zip(sUtimes,Vtimes):
    if i <= l(j)/float(L):
        nhpp.append(j)
snhpp = sorted(nhpp)                
N = []

for i in range(0,len(nhpp)):
    N.append(i)
        
plt.step(snhpp,N)
plt.show()
