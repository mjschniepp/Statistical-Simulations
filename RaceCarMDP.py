'''
    This is an implementation and expirimentation with Markov Decsion Processes
    Title: Race Car Game
    The objective is for the car to gain a distance of 100 (collect 100 'distance'
    points. Points are awarded depending on the decisions made. Riskier decisions 
    award more points but run the risk of losing points. 
    Choosing the fast option awards more points but runs the risk of the overheat state
    while choosing slow awards fewer points offering no risk of overheating. 
    The objective is to reach 100 points in as few steps as possible. 
    Here the control strategy is to choose cool everytime resulting in 100 
    points in 100 steps. Many other decision making strategies can be implemented
    and expirimented with at the users discretion if they wish to find the 
    more efficient strategy. The current strategy in test below is to choose slow
    for the first 90% percent distance, then choose only fast. 
'''

import numpy as np
import matplotlib.pyplot as plt

# Transition Probabilities
cool_fast = [0.2,0.8]
cool_slow = [1.0]
warm_fast = [0.2,0.8]
warm_slow = [0.3,0.7]
overheat = [1.0]

states = [1,2,3]



def random_pick(statesList, transMatrix):  # This function picks the state
    x = np.random.uniform(0, 1)
    cumulative_probability = 0.0
    for state, ij_prob in zip(statesList, transMatrix):
        cumulative_probability += ij_prob
        if x < cumulative_probability: break
    return state 
    

                                             
def race():
    # Transition Probabilities
    cool_fast = [0.2,0.8]
    cool_slow = [1.0]
    warm_fast = [0.2,0.8]
    warm_slow = [0.3,0.7]
    overheat = [1.0]

    states = [1,2,3]

    # initial fortune
    distance = 0
    goal = 100

    def random_pick(statesList, transMatrix):  # This function picks the state
        x = np.random.uniform(0, 1)
        cumulative_probability = 0.0
        for state, ij_prob in zip(statesList, transMatrix):
            cumulative_probability += ij_prob
            if x < cumulative_probability: break
        return state 
    
    n = 100
    steps = 0
    state = [1]
    endSteps = []
    while distance < goal+1:
        if state[0] == 1:
            state[0] = random_pick(states,cool_fast)
            distance += 2
        elif state[0] == 2 and distance <= (0.90)*goal:
            state[0] = random_pick(states,warm_slow)
            distance += 1
        elif state[0] == 2 and distance > (0.10)*goal:
            state[0] = random_pick(states[1:],warm_fast)
            distance += 3
        elif state[0] == 3:
            state[0] = 1
            distance += -4
        steps += 1
    return steps
          
endSteps = []
for i in range(0,1000):
    endSteps.append(race())

xbar = np.mean(endSteps) # mean number of steps to completion vs the control of 
std = np.std(endSteps)   # 100 steps
print('Strategy: .90/.10')
print('Mean',xbar)
print('Variance',np.var(endSteps))
print('Standard Deviation',std)

plt.hist(endSteps, bins = 30) # shows the histogram of completions steps
plt.show()

        
        
        