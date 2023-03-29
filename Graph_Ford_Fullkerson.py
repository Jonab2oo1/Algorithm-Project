# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 01:11:13 2023

@author: Jonab, Shatha, Dhuha, Faizah
"""
#____________________Algo"Ford-Fulkerson"_&_Graph______________________________

class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.target = v
    self.capacity = w

  def __repr__(self):
    return "%s-->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
  def  __init__(self):
    self.adj = {}
    self.flow = {}

  def AddVertex(self, vertex):
    self.adj[vertex] = []

  def GetEdges(self, v):
    return self.adj[v]

  def AddEdge(self, u, v, w = 0):
    if u == v:
      raise ValueError("u == v")
    edge = Edge(u, v, w)
    redge = Edge(v, u, 0)
    edge.redge = redge
    redge.redge = edge
    self.adj[u].append(edge)
    self.adj[v].append(redge)
    # Intialize all flows to zero
    self.flow[edge] = 0
    self.flow[redge] = 0

  def FindPath(self, source, target, path):
    if source == target:
      return path
    for edge in self.GetEdges(source):
      residual = edge.capacity - self.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = self.FindPath(edge.target, target, path + [(edge, residual)])
        if result != None:
          return result

  def MaxFlow(self, source, target):
    path = self.FindPath(source, target, [])
    print ('-' * 20)
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        self.flow[edge] += flow
        self.flow[edge.redge] -= flow
      path = self.FindPath(source, target, [])

    return sum(self.flow[edge] for edge in self.GetEdges(source))

import numpy as np
import pandas as pd

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
import time

g = FlowNetwork()
c = readFile()
print("Graph representation")
for i in range(len(c)):
  g.AddVertex(i)

for i in range(len(c)):
  for j in range(len(c[i])):
      if c[i][j]!=0:
        g.AddEdge(i,j,c[i][j])
print("Start Ford-Fulkerson")
start = time.process_time() 
print ("Ford-Fulkerson Max flow is ",g.MaxFlow(0, 5))
print("time ",time.process_time() - start )

