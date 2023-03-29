# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:23:48 2023

@author: Jonab, Shatha, Dhuha, Faizah
"""
#______________________Algo"Dinic's"_&_Adjacency Matrix________________________

import time
# Add a vertex to the set of vertices and the graph
def add_vertex(v):
    global graph
    global vertices_no
    global vertices
    if v in vertices:
        print("Vertex ", v, " already exists")
    else:
        vertices_no = vertices_no + 1
    
        vertices.append(v)
        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)
  

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

# Print the graph
def print_graph():
    global graph
    global vertices_no
    for i in range(vertices_no):
      for j in range(vertices_no):
        if graph[i][j] != 0:
          print(vertices[i], " -> ", vertices[j], \
          " edge weight: ", graph[i][j])


#function to read text graph file and convert to adjacency matrix
def read_graph(filename = "Algo_Dinic's_DATA.txt"):
    #matrix
    matrix = []
    
    #open file
    file = open(filename, "r")
    head = [next(file) for x in range(10)] # this 10 means it reads only 10 lines from the file. You can change it.
    #read each line convert to list
    for line in head:
        each_line = line.strip()
        print (each_line,"-------")
        #line_list = each_line.split()
        #print (type(line_list))
       
        types=[int,int,float]
        line_list = [f(x) for (f,x) in zip(types,each_line.split())]

        #append to matrix
        matrix.append(line_list)
    
    #close file
    file.close()
    
    #return
    return matrix


# extract first and second
# element of each sublist in a list of lists
def Extract(lst, index):
    return [item[index] for item in lst]


#call function read_graph and return to matrix
matrix = read_graph()    
graph = []
# stores the vertices in the graph
vertices = []


index = 0
verticies_1 = Extract(matrix, index)
index = 1
verticies_2 = Extract(matrix, index)

all_vertices = verticies_1 + verticies_2
unique = list(set(all_vertices))
vertices_no = 0 
for i in unique:
    add_vertex(i)
    
for k in matrix:
    a = int(k[0])
    b= int(k[1])
    w= float(k[2])
    add_edge(a,b,w)
    print(a,b,w)
 
print_graph()
print("Internal representation: ", graph)
#-----------------------------------------


#Dinic Algorithm

#build level graph by using BFS
def Bfs(C, F, s, t):  # C is the capacity matrix
        n = len(C)
        queue = []
        queue.append(s)
        global level
        level = n * [0]  # initialization
        level[s] = 1  
        while queue:
            k = queue.pop(0)
            for i in range(n):
                    if (F[k][i] < C[k][i]) and (level[i] == 0): # not visited
                            level[i] = level[k] + 1
                            queue.append(i)
        return level[t] > 0

#search augmenting path by using DFS
def Dfs(C, F, k, cp):
        tmp = cp
        if k == len(C)-1:
            return cp
        for i in range(len(C)):
            if (level[i] == level[k] + 1) and (F[k][i] < C[k][i]):
                f = Dfs(C,F,i,min(tmp,C[k][i] - F[k][i]))
                F[k][i] = F[k][i] + f
                F[i][k] = F[i][k] - f
                tmp = tmp - f
        return cp - tmp

#calculate max flow
#_ = float('inf')
def MaxFlow(C,s,t):
        n = len(C)
        F = [n*[0] for i in range(n)] # F is the flow matrix
        flow = 0
        while(Bfs(C,F,s,t)):
               flow = flow + Dfs(C,F,s,100)
        return flow

#-------------------------------------
# make a capacity graph
start = time.process_time()
source = 0  # A
sink = 5    # F  
print ("Dinic's Algorithm")
max_flow_value = MaxFlow(graph, source, sink)
print ("max_flow_value is", max_flow_value)
print("\nTotal time = ")
print(time.process_time() - start)