"""
********************************************************************************
** Authors:
** James Hippler (hipplerj@oregonstate.edu)
**
** Oregon State University
** CS 467-400 (Summer 2018)
** Online Capstone Project
**
** Project Group Lyra: Graphical Crawler (WEB2)
** Description: Python Crawler Application for Breadth-First/Depth-First URL
** web searches.
** Due: Friday, August 17, 2018
**
** Filename: graph.py
********************************************************************************
"""

class build_graph():

    def __init__(self):
        self.map = {}
        self.nodes = {}
        self.edges = {}
        self.graph = {}

    def add_nodes(self, node, url, color):
        color = { 'color': color }
        label = { 'label': node }
        self.nodes[url] = { 'url': url }
        self.nodes[url].update(color)
        self.nodes[url].update(label)

    def add_edges(self, node, edge):
        connection = { edge: {} }
        if node not in self.edges:
            self.edges[node] = connection
        else:
            self.edges[node].update(connection)

    def package_graph(self):
        self.graph['nodes'] = self.nodes
        self.graph['edges'] = self.edges
