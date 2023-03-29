# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:36:15 2023

@author: Jonab, Shatha, Dhuha, Faizah
"""
#______________________Algo"Edmonds-KARP"_&_2D Array and Queue_______________________

import time 

def edmonds_karp(C, source, sink):
    n = len(C) # C is the capacity matrix
    F = [[0] * n for i in range(n)]
    # residual capacity from u to v is C[u][v] - F[u][v]

    while True:
        path = bfs(C, F, source, sink)
        if not path:
            break
        # traverse path to find smallest capacity
        flow = min(C[u][v] - F[u][v] for u,v in path)
        # traverse path to update flow
        for u,v in path:
            F[u][v] += flow
            F[v][u] -= flow
    return sum(F[source][i] for i in range(n))

def bfs(C, F, source, sink):
    queue = [source]                 
    paths = {source: []}
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if C[u][v] - F[u][v] > 0 and v not in paths:
                paths[v] = paths[u] + [(u,v)]
                if v == sink:
                    return paths[v]
                queue.append(v)
    return None



 #colom3 wight  
datafile=open("Algo_Edmonds_KARP_DATA.txt", "r") 
w=datafile.read().split()[2::3]


for i in range(0,len(w)):
   
    w[i]=float(w[i])  

# wieht in 2d matrix
def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]

C=convert_1d_to_2d(w, 353)

C.pop(353)
source = 1  # A
sink = 200   # F
start = time.process_time() 
maxVal = edmonds_karp(C, source, sink)
print("max_flow_value is: ", maxVal)
print(time.process_time()-start)