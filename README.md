# Graphs
A first attempt to create a Graph manipulation package, written in Python.

Files:

Graph_v1.0.py
-------------
First implementation. The key idea is to store in each Vertex a dictionary with all its adjacent vertices.
Consists of two classes: Vertex, Graph. This implementation is without respect to additional attributes for
the edges other than their weight

Graph_v2.0.py
-------------
Optimized version of 1.0 with respect the edge's attributes (name, etc...). Here we have two lists:
vertices ['v1name', 'v2name', ...] and edges ['edge1name' [v1name, v2name, weight], ...]
