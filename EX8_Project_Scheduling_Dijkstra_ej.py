# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 08:35:44 2019

@author: Tomas
"""
# trying scipt dijstra implementation
# Altered version of https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
# to deal with the specific case of negative numbers to find largest path
import numpy as np

## Matrix with Negative numbers indicating cost of arcs, and positive 1 to indicate no arc
graph = np.array(  [[1,0,0,1,1,1,1,1],
                   [1,1,1,-14,-14,1,1,1],
                   [1,1,1,-3,1,1,1,1],
                   [1,1,1,1,1,1,-3,1],
                   [1,1,1,1,1,-7,1,1],
                   [1,1,1,1,1,1,-4,1],
                   [1,1,1,1,1,1,1,-10],
                   [1,1,1,1,1,1,1,1]])
    
## aux function to print result
def printSolution(dist, V): 
    print ("Vertex tDistance from Source")
    for node in range(V): 
        print (node,"t",dist[node]) 
    
# Funtion that implements Dijkstra's single source  
# shortest path algorithm for a graph represented  
# using adjacency matrix representation 
def dijkstra(graph,src): 
  
    # Save the number of nodes in variable V
    V = graph.shape[0]
    
    # Initialize the weights = inf and first node to 0 
    dist = [np.inf] * V
    dist[src] = 0
    sptSet = [False] * V 
 
    # Loop al the nodes in order
    for u in range(V): 
       
        # Mark the node u as visited
        sptSet[u] = True
        
        # Update dist value of the adjacent vertices  
        # of the picked vertex only if the current  
        # distance is greater than new distance 
        for v in range(V): 
            if graph[u][v] <= 0 and dist[v] > dist[u] + graph[u][v]: 
                    dist[v] = dist[u] + graph[u][v] 
        print(dist)
        print(sptSet)
  
    printSolution(dist, V) 

dijkstra(graph,0)


