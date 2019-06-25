"""  
        a
      b    c
    d     f  g
  h      i
print_by_level(node):

> a
> bc
> dfg
"""

'''
bfs 

1. queue = []
level = [] # add popped items from queue to level
target = 1
counter = 1 
2. first item in queue: add the root to the queue
3. while there are items in queue
counter += 1
if counter == target: 
    increase the target by twice as many as last level 
    print level
    reset level to [] 
4. pop the front of the queue 
5. if left and right child exist and add to queue 

'''


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


i = Node('i')
h = Node('h')
d = Node('d', left=h)
f = Node('f', left=i)
g = Node('g')
b = Node('b', left=d)
c = Node('c', left=f, right=g)
a = Node('a', left=b, right=c)

# tree object with node objects


def print_by_level(node):  # root passed in
    first_level = [node]
    levels = [first_level]

    while levels:
        current_level = levels.pop(0)
        print(''.join(node.data for node in current_level))
        next_level = []

        for node in current_level:
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)

        if len(next_level) > 0:
            levels.append(next_level)


def print_each_level(node):
    queue = [node]
    level = []

    counter = 0
    total = 1

    while queue: 
        current = queue.pop(0)
        counter += 1
        
        if current: 
            level.append(current.data)
             
            if current.left: 
                queue.append(current.left)
            else: 
                queue.append(None)
            
            if current.right: 
                queue.append(current.right)
            else: 
                queue.append(None)

        if counter == total:
            print(level)
            level = []  # reset level
            total = total * 2 + 1



print_each_level(a)
# print_by_level(a)


# https://coderpad.io/GGNHHYF2

'''
software architecture: 

distributed systems 
'''
