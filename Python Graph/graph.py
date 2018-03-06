import abc
import numpy as np

#########################################################################
"The Base class representation of a Graph with all the interface methods"
##########################################################################

class Graph(abc.ABC):

    def __init__(self,numVertices,directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self,v1,v2,weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self,v):
        pass

    @abc.abstractmethod
    def get_indegree(self,v):
        pass

    @abc.abstractmethod
    def get_edge_weight(selfself,v1,v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


############################################################################################
"Represent a graph as an adjacency matrix. A cell in the matrix has a  value when there exists an " \
"edge between the vertex represented by the row and the column numbers.Weighted graphs can hold values>1" \
"A value of 0 in the cell indicates that there is no edge"

#############################################################################################

class AdjacencyMatrixGraph(Graph):

    def __init__(self,numVertices,directed=False):
        super(AdjacencyMatrixGraph,self).__init__(numVertices,directed)

        self.matrix= np.zeros((numVertices,numVertices))

    def add_edge(self,v1,v2,weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError ("Vertices %d and %d are out of bounds" %(v1,v2))

        #Presently not dealing with negative edge
        if weight<1:
            ValueError("Edge Value cannot be less than 1 ")

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight


    def get_adjacent_vertices(self,v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" %v)

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices


    def get_indegree(self,v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self,v1,v2):
        return self.matrix[v1][v2]


    def display(self):
      for i in range(self.numVertices):
          for v in self.get_adjacent_vertices(i):
              print(i,"-->",v)


g=AdjacencyMatrixGraph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)


for i in range(4):
    print(g.get_adjacent_vertices(i))

g.display()

print("Directed Graph")
g=AdjacencyMatrixGraph(4,directed=True)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)


for i in range(4):
    print(g.get_adjacent_vertices(i))

g.display()
