"""
1.
Write an algorithm to find the 'next' node (i.e. in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.

2.
"""


def find_successor(node): 
    if node.right: 
        current = node.right
    else: 
        current = node 
        if current.parent:
            if current is current.parent.left: 
                return current.parent
            else: 
                # node has no successor because it is right of parent 
                # maybe not?
                return None 
        else: 
            # node has no successor because no parent and no left child 
            return None 
    
    # the left most node is successor 
    while current.left: 
        current = current.left 
    
    return current 
    
    
'''

     2 
  1     7
0     3   9

node = 3
output = 7

node = 1
output = 2

node = 2
output = 3 

node = 0 
output = 1

node = 7 
output = 9

disallow duplicates 
if no successor, return None 

pseudocode: 
1. get the right child (if it exists) 
  if not left child then check if there is a parent node 
2. from right child, get left child (if exists)
3. while there's a left child keep moving to left child
4. when there's no left child return current node 

'''