"""
    This is a code to implement and demomstrate a Markov Chain branching process
    (Population growth-type model) and to determine probability of extinction
    Warning: compuationally expensive and slow to compute. 
"""
import numpy as np


P = [0.25,0.25,0.50]
num_offsp = [0,1,2]

def random_pick(statesList, transMatrix):  # This function picks the state
    x = np.random.uniform(0, 1)
    cumulative_probability = 0.0
    for state, ij_prob in zip(statesList, transMatrix):
        cumulative_probability += ij_prob
        if x < cumulative_probability: break
    return state      
    
extinct = 0
for k in range(0,1000):
    Xlist = [1]
    y = 0
    for i in range(0,20):
        for j in range(0,Xlist[-1]):
            y += random_pick(num_offsp,P)
        if y == 0: break
        Xlist.append(y)
        y = 0
    if len(Xlist) < 21:
        extinct += 1
    
    
print (extinct / float(1000))

