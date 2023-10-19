#Given a connected, undirected, weighted graph, find a spanning tree using edges that minimizes the total weight . Use either Kruskal's or Prim's algorithm to find Minimum Spanning Tree (MST). You will printout edges of the tree and total cost of minimum spanning tree.
import time

class Graph:

    def __init__(self):
        self.V = 0
        self.graph = []

    def find(self, parent, u):
        if parent[u] == u:
            return u
        return self.find(parent, parent[u])
    
    def union(self, parent, rank, x, y):
        xRoot = self.find(parent, x)
        yRoot = self.find(parent, y)

        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot

        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1


    def kruskal(self):

        result = []
        e = 0
        i = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]

            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Edge \t\t Weight")
        print()
        res=0
        for u, v, weight in result:
            print(chr(u + 65), "-", chr(v + 65), "\t\t\t", weight)
            res+=weight
        print("The total Cost for the Minimum Spanning tree obtained is: ", res)
    
    def spanning_tree(self,file_num):
        print("The Minimum Spanning Tree input file: " + "inputText"+ str(file_num) + ".txt")
        fil = open("inputText"+str(file_num)+".txt", "r")
        i = 0
        for line in fil.readlines():
            x = line.split()
            if i == 0:
                self.V = int(x[0])
                self.graph = []
                print('Number of Vertices in the graph:',self.V)
                print('Number of Edges in the graph:', int(x[1]))
            elif len(x) == 1:
                pass
            else:
                self.graph.append([ord(x[0]) - 65, ord(x[1]) - 65, int(x[2])])
            i = i + 1
        startTime = time.time()
        self.kruskal()
        runTime = (time.time() - startTime) * 1000
        print('\nRuntime for the Algorithm in MilliSeconds: ',runTime)
        print("--------------------------------------------------")



print('\nMinimum Spanning Tree')

print("----------------------------------------------------------")

count = 0
G = Graph()
while(count < 4):
    if(count == 1 or count == 0):
        print("**************UnDirected Graph*************")
    else:
        print("**************Directed Graph*************")
    G.spanning_tree(count)
    count= count+1