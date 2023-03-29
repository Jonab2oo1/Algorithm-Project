# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:32:01 2023

@author: Jonab, Shatha, Dhuha, Faizah
"""
#_______________________Algo"Dinic's"_&_Adjacency List_________________________

class Node:
    def _init_(self, dest):
        self.dest = dest
        self.next = None

class LinkedList:
    def _init_(self, head=None):
        self.head = head
    
    def add_node(self, dest):
        new_node = Node(dest)
        new_node.next = self.head
        self.head = new_node

class Graph:
    def _init_(self, vertices):
        self.V = vertices
        self.graph = [LinkedList() for i in range(vertices)]
    
    def addEdge(self, src, dest):
        self.graph[src].add_node(dest)
    
    def read_from_file(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                src, dest = map(float, line.strip().split())
                self.addEdge(src, dest)
                
import time

start = time.process_time()

# Reading a sample graph from a text file
n = int(input("Enter the number of vertices: "))
g = Graph
g.read_from_file(filename = "Algo_Dinic's_DATA.txt")

# Printing the adjacency list representation of the graph
for i in range(g.V):
    print("Adjacency list of vertex {}:".format(i), end="")
    temp = g.graph[i].head
    while temp:
        print(" -> {}".format(temp.dest), end="")
        temp = temp.next
    print("\n") 

print("\nTotal time = ")
print(time.process_time()-start)