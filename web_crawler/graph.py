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
** Filename: search_state.py
**
** Example Form Return:
** {'starting_url': 'https://www.google.com', 'method': 'value', 'depth': 12, 'keyword': 'find me'}
********************************************************************************
"""

class build_graph():
    nodes = {}
    edges = {}

    def add_node(self, node):
        self.nodes.update(node)

    def add_edges(self, edges):
        for x in range(len(edges)):
            self.edges.update(edges[x])
