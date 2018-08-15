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
        self.nodes = {}
        self.edges = {}
        self.graph = {}

    def add_nodes(self, node, url, color, key_word_found, key_word):
        color = { 'color': color }
        label = { 'label': node }
        title = { 'title': node }
        keyword_found = { 'keyword_found': key_word_found}
        keyword = { 'keyword': key_word}
        self.nodes[url] = { 'url': url }
        self.nodes[url].update(color)
        self.nodes[url].update(label)
        self.nodes[url].update(title)
        self.nodes[url].update(keyword_found)
        self.nodes[url].update(keyword)

    def add_edges(self, node, edge):
        if edge == '':
            connection = {}
        else:
            connection = { edge: {} }
        if node not in self.edges:
            self.edges[node] = connection
        else:
            self.edges[node].update(connection)

    def package_graph(self):
        self.graph['nodes'] = self.nodes
        self.graph['edges'] = self.edges
