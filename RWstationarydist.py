#
# Michael Schniepp
# 
# Here we are implementing a Random Walk Markov Chain
# and approximating the stationary distribution of states. 

import numpy as np
import matplotlib.pyplot as plt


P1 = [0.5,0.3,0.2]  # These will act as the transition matrix
P2 = [0.1,0.4,0.5] 
P3 = [0.0,0.2,0.8]
states = [1,2,3]               

def random_pick(statesList, transMatrix):  # This function picks the state
    x = np.random.uniform(0, 1)
    cumulative_probability = 0.0
    for state, ij_prob in zip(statesList, transMatrix):
        cumulative_probability += ij_prob
        if x < cumulative_probability: break
    return state            

pathEnds = []
for j in range(0,10000):
    path = []
    initialState = np.random.randint(1,4)
    path.append(initialState)
    for i in range(0,10):
        if path[i] == 1:
            path.append(random_pick(states,P1))
        elif path[i] == 2:
            path.append(random_pick(states,P2))
        elif path[i] == 3:
            path.append(random_pick(states,P3))
    pathEnds.append(path[-1])
    
x1 = float(pathEnds.count(1)) / len(pathEnds) # offers the values of the 
x2 = float(pathEnds.count(2)) / len(pathEnds) # final state distribution
x3 = float(pathEnds.count(3)) / len(pathEnds) 
print( x1,x2,x3)

plt.hist(pathEnds, bins=np.arange(0,5,1))  # shows a historgram of the 
plt.show()                                 # final state distribution