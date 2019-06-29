# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:45:47 2019

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
# We need 1 matrix, the A_eq matrix that corresponds to the NA matrix.
NA, arcs = nodoNodoANodoArco(NN)
Aeq = NA

# load cost array of arcs dimensions and time array of same dimensions
C = np.array([2,1,2,5,2,1,2])
t = np.array([3,1,3,1,3,3,5])

# "linear equality constraint" of nodes dimensions. Equality constraints for each node for flow 
# and init max time T
T = 8 # From the exercise 
beq = np.array([1,0,0,0,0,-1])

## load bounds of arcs dimensions
bounds = np.zeros((C.shape[0])).astype(tuple)
for i in range(0, C.shape[0]):
    bounds[i] = (0,np.inf)
    
bounds = tuple(bounds)

# solve the linear prog for simplex and interior point

results = []     # Empty array for values of primal equation
landas = []      # Empty array for values of lambda
tolerance = 0.01 # Level of tolerance for the difference of lambda
landa = 0.01     # Init Lambda
landaNext = 0.01 # Init lambda Next = lambda
diff = np.inf    # Init difference to infinity
i = 1            # Init counter i, 1 for the step divisor.
# Loop while the difference between lambda_i and lambda_i+1 is less than the setted tolerance 
while diff > tolerance and i < 150:
    # Update Value of lambda for the lambda obtained in previous iteration
    landa = landaNext
    # Calculate the C~ = C + lambda*t  and minimize using linprog
    CplusLambdaT = C + landa * t
    res = lp(CplusLambdaT, A_eq=Aeq, b_eq=beq, bounds=bounds)
    # Calculate the primal value with the result of the minimization for plotting later
    primal = res.fun - T * landa    
    # Calculate the gradient of C*X + lambda(t*x + T)
    gradient = np.dot(t, res.x) - T
    # Update Value of step, inversily proportional to the index of iteration
    step = 1/i                          
    # Calculate the next lambda by moving the value "step" over the gradient 
    # and compute difference between current lambda
    landaNext = landa + step*gradient 
    diff = abs(landaNext - landa)
    # Update index value, and append calculated values to list for plotting later
    i += 1
    results.append(primal)
    landas.append(landa)
    print(i, step, gradient ,landa, landaNext, diff)

# shortcut, list of the number of steps to plot
steps = [s for s in range(1,i)]
    
## Plot of the different values per iteration
plt.subplot(211)
plt.plot(steps, results, marker="")
plt.axhline(y=max(results), color='r', linestyle='-')
plt.show()

plt.subplot(212)
plt.plot(steps, landas, marker="")
plt.axhline(y=landaNext, color='r', linestyle='-')
plt.show()






