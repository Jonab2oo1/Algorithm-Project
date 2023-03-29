# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:38:22 2023

@author: Jonab, Shatha, Dhuha, Faizah
"""

from collections import deque

#_______________________Algo"Dinic's"_&_Graph_________________________

class Dinic:
    def _init_(self, graph, source, sink):
        self.graph = graph
        self.source = source
        self.sink = sink
        self.n = len(graph)
        self.level = [-1]*self.n
        self.flow = 0
        
    def create_graph(file):
      graph = {}
      with open(file) as f:
          source, sink = map(int, f.readline().strip().split())
          for line in f:
              u, v, w = map(int, line.strip().split())
              if (u, v) not in graph:
                  graph[(u, v)] = int(w)
      return graph, source, sink

    def bfs(self):
        self.level = [-1]*self.n
        self.level[self.source] = 0
        q = deque([self.source])
        while q:
            u = q.popleft()
            for v, w in self.graph[u]:
                if self.level[v] == -1 and w > 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)

    def dfs(self, u, bottleneck):
        if u == self.sink:
            return bottleneck
        for i in range(len(self.graph[u])):
            v, w = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and w > 0:
                f = self.dfs(v, min(bottleneck, w))
                if f > 0:
                    self.graph[u][i] = (v, w-f)
                    self.graph[v].append((u, f))
                    return f
        return 0

    def max_flow(self):
        while True:
            self.bfs()
            if self.level[self.sink] == -1:
                return self.flow
            bottleneck = float('inf')
            while bottleneck > 0:
                bottleneck = self.dfs(self.source, float('inf'))
                self.flow += bottleneck
import time 

start = time.process_time()

graph, source, sink = Dinic.create_graph("Algo_Dinic's_DATA.txt")
dinic = Dinic(graph, source, sink)
max_flow = dinic.max_flow()
print("Maximum flow: ", max_flow)
print("\nTotal time = ")
print(time.process_time()-start)