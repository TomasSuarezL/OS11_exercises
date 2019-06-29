# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:28:28 2019

@author: Tomas
"""


import numpy as np
from scipy.optimize import linprog as lp

## load node to node matrix
NN = np.matrix([[0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
               [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
               [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
               [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
               [0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
               [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

# transform Node to Node matrix to Node Arc matrix, using the function made in basic utils EX0
NA, arcs = nodoNodoANodoArco(NN)

# Number of nodes of Plants, Stocks and Sale Points in order
pss = {"plants": 6, "stocks": 4, "sales": 6}

# Initialize Matrix of upper bounded constraints and equal constraints
Aub = np.zeros(NA.shape)
Aeq = np.zeros(NA.shape)
# Load values of Node Arc matriz into correspondix Matrix
Aub[:pss["plants"]+pss["stocks"], :] = NA[:pss["plants"]+pss["stocks"], :]
Aeq[pss["plants"]+pss["stocks"]:, :] = NA[pss["plants"]+pss["stocks"]:, :]


# load cost array of arcs dimensions
C = np.array([100,200,100,200,150,150,150,150,200,100,200,100,100,150,200,100,150,200,200,150,100,200,150,100])

# "linear equality constraint" of nodes dimensions
b = np.array([20,30,10,40,30,10,0,0,0,0,-30,-40,-10,-20,-20,-20])

# Initialize Split b to b for upper bound and b for equal constraints
bub = np.zeros(b.shape)
beq = np.zeros(b.shape)

bub[:pss["plants"]+pss["stocks"]] = b[:pss["plants"]+pss["stocks"]]
beq[pss["plants"]+pss["stocks"]:] = b[pss["plants"]+pss["stocks"]:]

## load bounds of arcs dimensions
#ubs = np.array([np.inf,np.inf,np.inf,np.inf,10,5,10,5,5,5,3,3,6,3,6,3,3,3,np.inf,np.inf,np.inf,np.inf,np.inf])
bounds = np.zeros((C.shape[0])).astype(tuple)
for i in range(0, C.shape[0]):
    bounds[i] = (0,np.inf)
    
bounds = tuple(bounds)

# solve the linear prog for simplex and interior point
res = lp(C, A_ub = Aub, A_eq=Aeq, b_ub=bub ,b_eq=beq, bounds=bounds)
res_ip = lp(C, A_eq=NA, b_eq=b, bounds=bounds, method='interior-point')




