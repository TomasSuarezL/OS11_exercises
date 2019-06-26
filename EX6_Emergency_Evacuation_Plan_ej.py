# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:38:18 2019

@author: Tomas
"""

import numpy as np
from scipy.optimize import linprog as lp

## load node to node matrix
NN = np.matrix([[0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
               [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

# transform Node to Node matrix to Node Arc matrix, using the function made in basic utils EX0
NA, arcs = nodoNodoANodoArco(NN)

# load cost array of arcs dimensions
C = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1])

# "linear equality constraint" of nodes dimensions
b = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

## load bounds of arcs dimensions
ubs = np.array([np.inf,np.inf,np.inf,np.inf,10,5,10,5,5,5,3,3,6,3,6,3,3,3,np.inf,np.inf,np.inf,np.inf,np.inf])
bounds = np.zeros((C.shape[0])).astype(tuple)
for i in range(0, C.shape[0]):
    bounds[i] = (0,ubs[i])
    
bounds = tuple(bounds)

# solve the linear prog for simplex and interior point
res = lp(C, A_eq=NA, b_eq=b, bounds=bounds)
res_ip = lp(C, A_eq=NA, b_eq=b, bounds=bounds, method='interior-point')


