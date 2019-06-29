# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:06:58 2019

@author: Tomas
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog as lp

## load node to node matrix
NN = np.array(    [[0,1,1,0,0,0],
                   [0,0,0,1,0,1],
                   [0,0,0,0,1,0],
                   [0,0,0,0,0,1],
                   [0,0,0,0,0,1],
                   [0,0,0,0,0,0]])

# transform Node to Node matrix to Node Arc matrix, using the function made in basic utils EX0
# We need 1 matrix, the A_eq matrix that corresponds to the NA matrix
NA, arcs = nodoNodoANodoArco(NN)
Aeq = NA

# load cost array of arcs dimensions
C = np.array([2,1,2,5,2,1,2])
t = np.array([3,1,3,1,3,3,5])

# "linear equality constraint" of nodes dimensions. Equality constraints for each node for flow 
# and max time T
T = 8 # From the exercise 
beq = np.array([1,0,0,0,0,-1])

## load bounds of arcs dimensions, in this case with no bounds -> lb = 0 and ub = infinity
bounds = np.zeros((C.shape[0])).astype(tuple)
for i in range(0, C.shape[0]):
    bounds[i] = (0,np.inf)
    
bounds = tuple(bounds)

# solve the linear prog for simplex and interior point
results = []                                    # Init empty array of results
landas = np.array([l/50 for l in range(51)])    # Generate array with values of lambda to calculate
# Loop for each value of lambda
for landa in landas:  
    # Calculate the C~ = C + lambda*t  and minimize using linprog
    CplusLambdaT = C + landa * t
    res = lp(CplusLambdaT, A_eq=Aeq, b_eq=beq, bounds=bounds)
    # Calculate the value of the primal equation C~*X - lambda * T
    primal = res.fun - T * landa
    # Append results to list to plot later
    results.append(primal)

# Plot results for each value of lambda
plt.stem(landas, results, use_line_collection=True, markerfmt=".")
plt.show()




