# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 01:06:34 2023

@author: Jonab, Shatha, Dhuha, Faizah
"""
#____________________Algo"Ford-Fulkerson"_&_Adjacency_Array____________________


import pandas as pd
import numpy as np
import time


def BFS(graph, s, t, parent):
    # Return True if there is node that has not iterated.
    visited = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False


def FordFulkerson(graph, source, sink):
    # This array is filled by BFS and to store path
    parent = [-1] * (len(graph))
    max_flow = 0
    while BFS(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink

        while s != source:
            # Find the minimum value in select path
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow
def readFile():
    data = pd.read_csv("Algo_Ford_Fullkerson_DATA.txt", sep="\t")
    data.columns=["from","to","w"]
    adj = np.zeros((data["to"].max()+1,data["to"].max()+1),dtype=np.float32)
    fromList=data["from"].to_list()
    toList=data["to"].to_list()
    wList=data['w'].to_list()
    for i,j,z in zip(fromList,toList,wList):
      adj[i-1][j-1]=z
      #adj[j - 1][i - 1] = z
    return  adj

print("Adjacency Array representation ")
C = readFile()
print("done Load Adj Array form file")
source = 0
sink = 5
start = time.process_time() 
max_flow_value = FordFulkerson(C, source, sink)
print ("Ford-Fulkerson Max flow is ",max_flow_value)
print("time ",time.process_time() - start)