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
** Filename: depth_traversed.py
**
** External Resources:
** - https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
** - https://stackoverflow.com/questions/1080411/retrieve-links-from-web-
**   page-using-python-and-beautifulsoup
** - https://stackoverflow.com/questions/1936466/beautifulsoup-grab-
**   visible-webpage-text
********************************************************************************
"""

from collections import defaultdict

class Stack:
     def __init__(self):
         self.nodes = []
         self.visited = []
         self.map = defaultdict(list)

     def push(self, item):
         self.nodes.append(item)

     def pop(self):
         return self.nodes.pop()

     def peek(self):
         return self.nodes[len(self.nodes) - 1]

     def size(self):
         return len(self.nodes)
