#Given a directed graph G  with n  vertices and m edges. This graph may not be simple. Decompose this graph into Strongly Connected Components (SCCs) and print the components. You can use the same input format defined below.
import time
from collections import defaultdict
   
#Class for graphs
class Graph:

    def __init__(self):
        self.V= 0 #No. of vertices
        self.graph = defaultdict(list) #  Dictionary to store graph


    # function for adding an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
        
    # Function that returns reverse of this graph
    def transposeGraph(self):
        g = Graph()
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
    

    def fillOrder(self,v,visited, stack):
        # Marking the current node as visited 
        visited[v]= True
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
      
    
    # A function used by DFS
    def DFSutil(self,v,visited):
        # Mark the current node as visited and print it
        visited[v]= True
        k=v+65
        print(chr(k))
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSutil(i,visited)
    
    
    # The main function that finds and prints all strongly connected components
    def printSCC(self):
          
        stack = []
        visited =[False]*(self.V)
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
  
        gr = self.transposeGraph()
        
        visited =[False]*(self.V)
        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.DFSutil(i, visited)
                print("")
    

    def strongly_connected(self,file_num):
        print("The Strongly Connected Components input file:" + "inputText" + str(file_num) + ".txt")

        f1 = open("inputText"+str(file_num)+".txt", "r")
        i = 0
        
        for line in f1.readlines():
            x = line.split()
            if i == 0:
                self.V = int(x[0])
                self.graph = defaultdict(list)
                print("Number of Vertices in the graph:", self.V)
                print("\nEdges of the Graph\n")
                
            elif len(x) == 1:
                pass
            else:
                print(x[0]+"-"+x[1])
                self.addEdge(ord(x[0]) - 65, ord(x[1]) - 65)
            i = i + 1
        print ("The strongly connected components in given graph are: ")

        startTime = time.time()
        self.printSCC()
        
        runTime = (time.time() - startTime) * 1000
        
        print('\nRuntime for the Algorithm in MilliSeconds: ',runTime)


print('\n Strongly Connected Components')
print("----------------------------------------------")


count = 2
G = Graph()
while(count < 6):
    print("**************Directed Graph*************")
    G.strongly_connected(count)
    count= count+1
