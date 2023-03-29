# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:29:18 2023

@author: Jonab, Shatha, Dhuha, Faizah
"""

#____________________Algo"Edmonds-KARP"_&_Graph and Queue______________________

import time 
#from collections import defaultdict



'''
Part of Cosmos by OpenGenus Foundation
'''

#This class represents a directed graph using adjacency matrix representation
class Graph:
    def _init_(self,graph):
        self.graph = graph # residual graph
        self. ROW = len(graph)
        #self.COL = len(gr[0])   
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent):
        # Mark all the vertices as not visited
        visited =[False]*(self.ROW)     
        # Create a queue for BFS
        queue=[]      
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        # Standard BFS Loop
        while queue: 
            #Dequeue a vertex from queue and print it
            u = queue.pop(0)
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and float(val) > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False    
    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
        max_flow = 0 # There is no flow initially
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            # Add path flow to overall flow
            max_flow +=  path_flow
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow
 
 
# Create a graph given in the above diagram


 #colom3 wight  
datafile=open("Algo_Edmonds_KARP_DATA.txt", "r") 
w=datafile.read().split()[2::3]


for i in range(0,len(w)):
   
    w[i]=float(w[i])  

# wieht in 2d matrix
def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]

test=convert_1d_to_2d(w, 353)



start = time.process_time() 

g= Graph(test)   
print("the source:1")
source = 1
print("Enter the sink: 200")
sink = 200

print("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
print(time.process_time()-start)