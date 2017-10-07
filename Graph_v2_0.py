'''
Created on 06/10/2017

@author: moodyAllen
'''

from memoization import *

class Edge:
    """ The class for the edges of the graph
        to be used by class Graph """
    def __init__(self, id)
    ' id denotes the name and con the connection it creates  '
        self.id = id
        self.con = ()

    def __str__(self):
        return str(self.id) + "connects " + str(self.con[0]) + " with " + str(self.con[1]) + ", distance = " + str(self.con[2])

    def add_connection(self, con):
    ' we expect new to be a tupple '
    self.con = con

    def connects(self):
        return (self.con[0], self.con[1])

    def get_id(self):
        return self.id

    def get_weight(self):
        return self.adj[2]

class Graph:

    def __init__(self, directed = True, weighted = True):
        self.vertices = []
        self.edges = []
        self.directed = directed
        self.weighted = weighted
        self.total_vertices = 0

    def __iter__(self):
        return iter(self.vertices)

    def add_vertex(self, node):
        """ Adds a vertex to the graph """
        self.total_vertices += 1
        self.vertices.append(node)

    def add_edge(self, id, con):
        """ Adds an edge to the graph
            note that con is a tupple """
        if self.id not in self.edges:
            self.total_edges += 1
            new_edge = Edge(id)
            new_edge.add_connection(con)
            self.edges.append(new_edge)
        
    def get_vertices(self):
        return self.vertices

    def get_adjacent(self, vertex):
        result = ()
        for key in self.edges:
            if key.connects()[0]== vertex:
                result.append((key.connects()[1], key.get_weight())
