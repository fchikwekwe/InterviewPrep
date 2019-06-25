"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 

Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: 
[3,4,5,1,3,null,1]
[8,9,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""

# 2 * index + 1 to get left child
# 2 * index + 2 to get right child


# Pseudocode
'''
Pseudocode 
- max_vals = []
- loop over all nodes and add to queue
    - for node in queue 
    - create a robbed_houses set {}
    - traverse all other nodes (while there are nodes in tree to check)
        - check that node is neither parent nor child of any node in robbed houses
            if not: then add value and add node to robbed houses 
    - add the total value to max vals, 
    return the max of max_vals 
        write a more complicated algo to keep vals in order 
'''


def max_robbery(tree):
    max_vals = []
    for node_index, node in enumerate(tree):
        if node:
            # store houses robbed on that night w/ index in dict
            robbed_houses = {}
            robbed_houses[node_index] = node

            for i in range(len(tree)):
                for ind, node in robbed_houses:
                    left_child = 2 * ind + 1  # index
                    right_child = 2 * ind + 2
                if ind == 1 or ind == 2:
                    parent = 0
                elif ind % 2 == 1:  # odd
                    parent = (ind - 1) / 2
                else:  # even
                    parent = (ind - 2) / 2

                if i == left_child or i == right_child and i != parent:
