# BFS
#using Queue
import queue
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.admatrix=[[0 for i in range(vertices)] for j in range(vertices)]

    def addEdge(self,v1,v2):
        self.admatrix[v1][v2]=1
        self.admatrix[v2][v1]=1

    def remove(self,v1,v2):
        if self.containEdge(v1,v2) is False:
            return
        self.admatrix[v1][v2]=0
        self.admatrix[v2][v1]=0

    def bfs(self):
        visited=[False for i in range(self.vertices)]
        q=queue.Queue()
        q.put(0)
        visited[0]=True
        while q.empty() is False:
            u=q.get()
            print(u)    
            for i in range(self.vertices):
                if self.admatrix[u][i]>0 and visited[i]==False:
                    q.put(i)
                    visited[i]=True
        
    def containEdge(self,v1,v2):
        return True if self.admatrix[v1][v2]>0 else False

    def __str__(self):
        return str(self.admatrix)


g=Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,3)

g.bfs()
