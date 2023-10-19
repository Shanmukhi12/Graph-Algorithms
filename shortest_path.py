
# Find shortest path tree in both directed and undirected weighted graphs for a given source vertex. 
# Assume there is no negative edge in your graph.
import sys
import time
from collections import defaultdict

#Class for graphs
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.directed = False

    def findMinKey(self, distance, visited):
        min = float('inf')
        index = -1
        for k in self.graph.keys():
            if visited[k] is False and distance[k] < min:
                min = distance[k]
                index = k
        return index

    def dijkstra(self, src):
        visited = {i: False for i in self.graph}
        distance = {i: float('inf') for i in self.graph}
        parent = {i: None for i in self.graph}

        distance[src] = 0

        # find shortest path for all vertices
        for i in range(len(self.graph) - 1):
            u = self.findMinKey(distance, visited)
            visited[u] = True
            for v, w in self.graph[u]:

                if visited[v] is False and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    parent[v] = u
        return parent, distance
    
    #function to print path
    def printPath(self, parent, v):
        if parent[v] is None:
            return
        self.printPath(parent, parent[v])
        print(chr(v+65),end=" ")
        
        
    #function to print solution
    def printSolution(self, distance, parent, src):
        print('{}\t{}\t{}'.format('Vertex', '\tDistance', 'Path'))

        for i in self.graph.keys():
            if i == src:
                continue
            if  distance[i]==float("inf"):
                continue
            print('{} -> {}\t\t{}\t\t{}'.format(chr(src+65), chr(i+65), distance[i], chr(src+65)), end=' ')
            self.printPath(parent, i)
            print()
    
    def shortest_path(self, file_num):
        fil = open("inputText"+str(file_num)+".txt","r")
        i=0
        src=sys.maxsize

        print("Shortest paths input file:", "inputText"+str(file_num)+".txt")
        print()

        for line in fil.readlines():

            x = line.split()
            if i==0:
                noOfVertices=int(x[0])
                self.graph = defaultdict(list)
                print('Number of Vertices in the graph:',noOfVertices)
                print('Number of Edges in the graph:', int(x[1]))
                dir = x[2]
                if dir=="U":
                    self.directed = False
                else:
                    self.directed=True

            elif len(x)==1:
                src=ord(x[0])-65
            else:
                s = ord(x[0])-65
                d = ord(x[1])-65
                weight = int(x[2])

                self.graph[s].append([d, weight])

                if self.directed is False:
                    self.graph[d].append([s, weight])
                elif self.directed is True:
                    self.graph[d] = self.graph[d]
            i=i+1
            
        print("Source:",chr(src+65))
        if dir=="U":
            print("The Graph type is: " + "UNDIRECTED")
        elif dir=="D":
            print("The Graph type is: " + "DIRECTED")

        startTime = time.time()
        parent, distance = self.dijkstra(src)
        self.printSolution(distance, parent, src)
        runTime = (time.time() - startTime) * 1000

        print('\nRuntime for the Algorithm in MilliSeconds: ',runTime)
        print("********************************************************************")

print()
print('\n Single-Source Shortest Path Algorithm')

print("---------------------------------------------------")

count = 0
G = Graph()
while(count < 4):
    print("1. Directed")
    print("2. Undirected")
    gType = int(input( "Select the type of graph:"))
    if(gType == 1):
        print("Choose any file below")
        print("2. inputText2.txt")
        print("3. inputText3.txt")
        file_num = int(input("select the inputTestFile number   : "))
    if(gType == 2):
        print("Choose any file below")
        print("0. inputText0.txt")
        print("1. inputText1.txt")
        file_num = int(input("select the inputTestFile number   : "))
    G.shortest_path(file_num)
    count= count+1
