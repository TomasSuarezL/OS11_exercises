# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:47:59 2019

@author: Tomas
"""

import numpy as np
from scipy.optimize import linprog as lp

## load node to node matrix
NN = np.matrix([[0,1,1,0,0,0,0,0],
               [0,0,0,1,1,0,0,0],
               [0,0,0,1,0,0,0,0],
               [0,0,0,0,0,0,1,0],
               [0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,1,0],
               [0,0,0,0,0,0,0,1],
               [0,0,0,0,0,0,0,0]])

# Map Node Node matrix to Node Arc
NA, arcs = nodoNodoANodoArco(NN)

# load cost array of arcs dimensions with negative values to use minimize (linprog) to find larger path 
C = np.array([0,0,-14,-14,-3,-3,-7,-4,-10])

# "linear equality constraint" of nodes dimensions
b = np.array([1,0,0,0,0,0,0,-1])

## load bounds of arcs dimensions, in this case there is no bounds -> (0,inf)
bounds = np.zeros((C.shape[0])).astype(tuple)
for i in range(0, C.shape[0]):
    bounds[i] = (0,np.inf)
    
bounds = tuple(bounds)

# Resolve problem using linprog
res = lp(C, A_eq=NA ,b_eq=b, bounds=bounds)
res_ip = lp(C, A_eq=NA, b_eq=b, bounds=bounds, method='interior-point')








