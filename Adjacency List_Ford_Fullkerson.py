# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 01:06:53 2023

@author: Jonab, Shatha, Dhuha, Faizah
"""
#___________Algo"Ford-Fulkerson"_&_Adjacency_List______________________________

class Edge:
    def __init__(self, v1, v2, capacity, flow):
        self.from1 = v1
        self.to1 = v2
        self.capacity = capacity
        self.residual = []
        self.flow = flow

    def isResidual(self):
        return self.capacity == 0

    def remaining_capacity(self):
        return self.capacity - self.flow

    def augment(self, bottleneck):
        self.flow = self.flow+ bottleneck
        self.residual.flow =self.residual.flow - bottleneck
        # self.residual.capacity =- bottleneck
        # self.capacity =- bottleneck
        # self.residual.capacity =- bottleneck


class Graph:
    def __init__(self, numvertices):
        self.m = numvertices
        self.graph = []
        self.initialize_empty_flow_graph()

    def initialize_empty_flow_graph(self):
        for i in range(self.m):
            self.graph.append([])

    def add_edge(self, v1, v2, capacity, flow):
        e1 = Edge(v1, v2, capacity, flow)
        e2 = Edge(v2, v1, 0, flow)

        e1.residual = e2
        e2.residual = e1
        self.graph[v1].append(e1)

        self.graph[v2].append(e2)


class ford_fulkerson:
    def __init__(self, Graph, numvertices):
        # self.n = numvertices
        self.n = numvertices
        self.s =  0 # source index
        self.t = 40 # sink index
        self.visitedToken = 0
        # self.visited = list(range(0,self.n))
        self.visited = list(range(100, n + 100))
        # self.visited = list(range(-self.n, 0))
        self.minCut = [False] * self.n
        self.maxFlow = 0

    def solve(self, Graph):

        while True:
            f = self.dfs(Graph, self.s, flow=float("inf"))
            self.visitedToken = self.visitedToken + 1
            self.maxFlow = self.maxFlow + f
            if f == 0:
                break
        return self.maxFlow

    def dfs(self, Graph, node, flow):
        # print()
        if (node == self.t):
            return flow

        self.visited[node] = self.visitedToken
        edges = Graph.graph[node]
        for edge in edges:
            if (edge.remaining_capacity() > 0 and self.visited[edge.to1] != self.visitedToken):
                bottleneck = self.dfs(Graph, edge.to1, min(flow, edge.remaining_capacity()))
                if (bottleneck > 0):
                    edge.augment(bottleneck)
                    return bottleneck
        return 0

import pandas as pd
import numpy as np
import time

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
print("Adjacency List representation ")
c = readFile()
n = len(c)
g = Graph(n)
flow = 0
for i in range(n):
  for j in range(n):
      if c[i][j]!=0:
        g.add_edge(i,j,c[i][j],flow)
print("Done setting the ADj list")
ford = ford_fulkerson(g,n)
ford.s=0
ford.t =5 
start = time.process_time() 
maxFlow=ford.solve(g)
print ("Ford-Fulkerson Max flow is ",maxFlow)
print("time ",time.process_time()-start)