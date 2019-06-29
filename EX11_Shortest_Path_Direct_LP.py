# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 09:23:54 2019

@author: Tomas
"""
import numpy as np
from scipy.optimize import linprog as lp

## load node to node matrix
NN = np.array(    [[0,1,1,0,0,0],
                   [0,0,0,1,0,1],
                   [0,0,0,0,1,0],
                   [0,0,0,0,0,1],
                   [0,0,0,0,0,1],
                   [0,0,0,0,0,0]])

# transform Node to Node matrix to Node Arc matrix, using the function made in basic utils EX0
# We need 2 matrix, the A_eq matrix that corresponds to the NA matrix, and the time constraint array
NA, arcs = nodoNodoANodoArco(NN)
Aeq = NA
Aub = [[3,1,3,1,3,3,5]]


# load cost array of arcs dimensions
C = np.array([2,1,2,5,2,1,2])

# "linear equality constraint" of nodes dimensions. Equality constraints for each node for flow 
# and upper bound for total time constraint T
T = 8 # From the exercise 
beq = np.array([1,0,0,0,0,-1])
bub = [T]

## load bounds of arcs dimensions
bounds = np.zeros((C.shape[0])).astype(tuple)
for i in range(0, C.shape[0]):
    bounds[i] = (0,np.inf)
    
bounds = tuple(bounds)

# solve the linear prog for simplex and interior point
res = lp(C, A_eq=Aeq, b_eq=beq, A_ub=Aub, b_ub=bub, bounds=bounds)





