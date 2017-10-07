'''
Created on 06/10/2017

@author: moodyAllen
'''

from memoization import *

class Graph:

    def __init__(self, directed = True, weighted = True):
        self.vertices = []
        self.edges = []
        self.directed = directed
        self.weighted = weighted
        self.total_vertices = 0

    def add_vertex(self, node):
        """ Adds a vertex to the graph """
        self.total_vertices += 1
        self.vertices.append(node)
