from collections import defaultdict

class Traversed:
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
