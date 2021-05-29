#Graph
#use Adjacent list when there are less vertices
#use Adjacent matrix when no. of vertices is more

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.Admatrix=[[0 for i in range(vertices)] for j in range(vertices)]

    def AddEdge(self,v1,v2):
        self.Admatrix[v1][v2]=1
        self.Admatrix[v2][v1]=1

    def removeEdge(self,v1,v2):
        if self.ContainEdge(v1,v2) is False:
            return
        self.Addmatrix[v1][v2]=0
        self.Addmatrix[v2][v1]=0

    def ContainEdge(self,v1,v2):
        return True if self.Admatrix[v1][v2] > 0 else False

    def __str__(self):
        return str(self.Admatrix)

g=Graph(5)
g.AddEdge(0,1)
g.AddEdge(1,3)
g.AddEdge(2,4)
print(g)
    
        
