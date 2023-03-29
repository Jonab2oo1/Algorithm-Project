# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:34:34 2023

@author: Jonab, Shatha, Dhuha, Faizah
"""

#______________________Algo"Edmonds-KARP"_&_2D Array and stack_______________________

import time 

def bfs(C, F, s, t):
    stack = [s]
    paths={s:[]}
    if s == t:
            return paths[s]
    while(stack):
            u = stack.pop()
            for v in range(len(C)):
                    if(C[u][v]-F[u][v]>0) and v not in paths:
                            paths[v] = paths[u]+[(u,v)]
                            if v == t:
                                    return paths[v]
                            stack.append(v)
    return None

def maxFlow(C, s, t):
    n = len(C) # C is the capacity matrix
    F = [[0] * n for i in range(n)]
    path = bfs(C, F, s, t)
    while path != None:
        flow = min(C[u][v] - F[u][v] for u,v in path)
        for u,v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C,F,s,t)
    return sum(F[s][i] for i in range(n))

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
maxVal = maxFlow(C, source, sink)
print("max_flow_value is: ", maxVal)
print(time.process_time()-start)