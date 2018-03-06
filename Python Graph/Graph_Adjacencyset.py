import abc

class Graph(abc.ABC):
    def __init__(self,numberOfVertex,directed=False):
        self.numberOfVertex =  numberOfVertex
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
    def display(self):
        pass


class Node:
    def __init__(self,vertexID):
        self.vertexID = vertexID
        self.adjacency_set = set()

    def add_edge(self,v):
        if self.vertexID == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" %v)

        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)


class AdjacencySetGraph(Graph):

    def __init__(self,numberOfVertex,directed=False):
        super(AdjacencySetGraph,self).__init__(numberOfVertex,directed)

        self.vertex_list = []
        for i in range (numberOfVertex):
            self.vertex_list.append(Node(i))

    def add_edge(self,v1,v2,weight=1):
        if v1 >= self.numberOfVertex or v2 >= self.numberOfVertex or v1 < 0 or v2 < 0:
            raise ValueError ("Vertices %d and %d are out of bounds" %(v1,v2))

        if weight !=1:
            raise ValueError("An adjaceny set cannot be represent edge weight > 1")

        self.vertex_list[v1].add_edge(v2)

        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self,v):
        if v<0 or v>= self.numberOfVertex:
            raise ValueError("Cannot access vertex %d" %v)

        return self.vertex_list[v].get_adjacent_vertices()


    def get_indegree(self,v):
        if v<0 or v>= self.numberOfVertex:
            raise ValueError("Cannot access vertex %d" %v)

        indegree = 0
        for i in range (self.numberOfVertex):
            if v in self.get_adjacent_vertices(i):
                indegree = indegree +1

        return indegree


    def display(self):
      for i in range(self.numberOfVertex):
          for v in self.get_adjacent_vertices(i):
              print(i,"-->",v)


g=AdjacencySetGraph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)


for i in range(4):
    print(g.get_adjacent_vertices(i))

g.display()

print("Directed Graph")
g=AdjacencySetGraph(4,directed=True)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)


for i in range(4):
    print(g.get_adjacent_vertices(i))

g.display()
