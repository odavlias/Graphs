'''
Created on 23/09/2017

@author: moodyAllen
'''

'''
Vertex class
contains a name for the vertex and
a dictionary of adjacent vertices
'''
class Vertex:

    def __init__(self, node):
        self.name = node
        self.adjacent = {}

    'print function'
    def __str__(self):
            return str(self.name) + ' adjacent vertices: ' + str([x.name for x in self.adjacent])

    'utility functions'
    def add_to_adjacents(self, new, weight):
        self.adjacent[new] = weight

    'getters'
    def get_connections(self):
        return self.adjacent.keys()

    def get_name(self):
        return self.name

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

'''
Graph class
contains a dictionary of the vertices, the total number of vertices
and informations about the graph (directed, weighted default=True)
'''
class Graph(object):

    def __init__(self, directed = True, weighted = True):
        self.vertices = {}
        self.total_vertices = 0
        self.directed = directed
        self.weighted = weighted

    def __iter__(self):
        return iter(self.vertices.values())

    'add and get vertex functions'
    def add_vertex(self, node):
        self.total_vertices +=1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def get_vertex(self, name):
        if name in self.vertices:
            return self.vertices[name]
        else:
            return None

    'add edge function'
    def add_edge(self, v1, v2, weight=1):
        'check if the connected vertices are already in the graph and add them if not'
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)

        'equalize the weights if the graph is not weighted'
        if self.weighted == False:
            weight = 1

        'update the neighborhood of v1'
        self.vertices[v1].add_to_adjacents(self.vertices[v2], weight)

        'update the neighborhood of v2 only if the graph is not directed'
        if self.directed == False:
            self.vertices[v2].add_to_adjacents(self.vertices[v1], weight)

    'get all vertices function'
    def get_vertices(self):
        return self.vertices.keys()
        

'''
Execution instance
'''
if __name__ == '__main__':

    my_graph = Graph()

    my_graph.add_vertex('A')
    my_graph.add_vertex('B')
    my_graph.add_vertex('C')
    my_graph.add_vertex('D')
    my_graph.add_vertex('E')
    my_graph.add_vertex('F')
    my_graph.add_vertex('G')
    my_graph.add_vertex('H')
    my_graph.add_vertex('I')
    my_graph.add_vertex('J')
    my_graph.add_vertex('K')

    my_graph.add_edge('A', 'B', 35)
    my_graph.add_edge('A', 'C', 30)
    my_graph.add_edge('B', 'D', 14)
    my_graph.add_edge('B', 'E', 12)
    my_graph.add_edge('C', 'E', 44)
    my_graph.add_edge('C', 'F', 4)
    my_graph.add_edge('C', 'G', 28)
    my_graph.add_edge('D', 'H', 9)
    my_graph.add_edge('E', 'I', 26)
    my_graph.add_edge('E', 'J', 38)
    my_graph.add_edge('F', 'J', 2)
    my_graph.add_edge('G', 'K', 20)
    my_graph.add_edge('K', 'J', 16)

    for v in my_graph:
        for w in v.get_connections():
            vid = v.get_name()
            wid = w.get_name()
            print(vid, wid, v.get_weight(w))

    for v in my_graph:
        print(my_graph.vertices[v.get_name()])
