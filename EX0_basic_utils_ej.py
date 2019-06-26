# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:37:40 2019

@author: Tomas
"""
import numpy as np

# Matriz Nodo a Nodo
NN = np.matrix([[0,1,1,0,0,0],
               [0,0,0,1,0,1],
               [0,0,0,1,0,0],
               [0,0,0,0,0,1],
               [0,0,0,0,0,1],
               [0,0,0,0,0,0]])

NZ = np.zeros((NN.shape[0], NN.sum()))


zcount = 0
for i in range(0,NN.shape[0]):
    for j in range(0, NN.shape[1]):
        if NN[i,j] > 0:
            NZ[i,zcount] = 1
            NZ[j,zcount] = -1
            zcount += 1
            print(i,j,zcount)


def nodoNodoANodoArco(NNmatrix):
    # save number of Arcs in variable, init matrix with zeroes
    numArcs = NNmatrix.sum()
    NZ = np.zeros((NNmatrix.shape[0], numArcs))
    zcount = 0
    arcLabels = ["" for x in range(numArcs)]
    
    # Loop the NodeNode matrix first row then column
    for i in range(0,NNmatrix.shape[0]):
        for j in range(0, NNmatrix.shape[1]):
            if NNmatrix[i,j] > 0:
                NZ[i,zcount] = 1
                NZ[j,zcount] = -1
                arcLabels[zcount] = str(i) + str(j)
                print(str(i) + '-' + str(j))
                zcount += 1
    return NZ , arcLabels
    
NN2 = np.matrix([[0,1,0,0],
               [1,0,0,1],
               [1,0,0,0],
               [0,0,0,0]])

NA = nodoNodoANodoArco(NN2)


array = []






