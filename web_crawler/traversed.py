from collections import defaultdict

class Traversed:
     def __init__(self):
         self.items = []
         self.visited = []
         self.map = defaultdict(list)

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
