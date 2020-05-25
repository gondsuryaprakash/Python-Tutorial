'''class AdjNode:
    def __init__(self,data):
        self.vertex=data
        self.next=None
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[None]*self.V
    # Function to add the(it
    def add_edge(self,src,dest):
        # Adding the destination in the source
        node=AdjNode(dest)
        node.next=self.graph[src]
        self.graph[src]=node

        # Adding the source in the destination
        node=AdjNode(src)
        node.next=self.graph[dest]
        self.graph[dest]=node
    #function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i),end=' ')
            tmp=self.graph[i]
            while tmp:
                print("-> {}".format(tmp.vertex),end=" ")
                tmp=tmp.next
            print("\n")
'''

# BFS Traversal of Graph
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def bfs(self,s):
        visited=[False]*(len(self.graph))
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if visited==False:
                    queue.append(i)
                    visited[i]=True
g= Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.bfs(2)


