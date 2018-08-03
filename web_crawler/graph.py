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
    visited = []
    nodes = {}
    edges = {}

    def add_nodes(self, node, url):
        print()
        if not node in self.nodes.values():
            self.nodes[node] = { 'url': url }
        else:
            self.nodes[node].update(node)
        # if keyword:
        #     self.nodes[title].update({ 'keyword': 'I am a keyword' })

    def add_edges(self, node, edge):
        if not node in self.edges.values():
            self.edges[node] = { edge: {} }
        else:
            new_connection = { edge: {} }
            self.edges[node].update(new_connection)


    def package_graph(self):
        graph = {}
        graph.update(self.nodes)
        graph.update(self.edges)
        return graph
