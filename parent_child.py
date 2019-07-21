# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

# For example, in this diagram, 6 and 8 have a common ancestor of 4.

# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   10

# parentChildPairs1 = [
#     (1, 3), (2, 3), (3, 6), (5, 6),
#     (5, 7), (4, 5), (4, 8), (8, 10)
# ]

# Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

# Sample input and output:

# hasCommonAncestor(parentChildPairs1, 3, 8) => false
# hasCommonAncestor(parentChildPairs1, 5, 8) => true
# hasCommonAncestor(parentChildPairs1, 6, 8) => true
# hasCommonAncestor(parentChildPairs1, 1, 3) => false
# hasCommonAncestor(parentChildPairs1, 6, 5) => true

# Additional example: In this diagram, 4 and 8 have a common ancestor of 10.

#       10
#      /  \
# 1   2    5
#  \ /    / \
#   3    6   7
#    \        \
#     4        8

# parentChildPairs2 = [
#     (10, 2), (10, 5), (1, 3), (2, 3),
#     (3, 4), (5, 6), (5, 7), (7, 8)
# ]

# hasCommonAncestor(parentChildPairs2, 4, 8) => true
# hasCommonAncestor(parentChildPairs2, 1, 6) => false


parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (8, 10)
]

parent_child_pairs_2 = [
    (10, 2), (10, 5), (1, 3), (2, 3),
    (3, 4), (5, 6), (5, 7), (7, 8)
]

#
# pseudocode
# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   10

# parentChildPairs1 = [
#     (1, 3), (2, 3), (3, 6), (5, 6),
#     (5, 7), (4, 5), (4, 8), (8, 10)
# ]
# {10: {8,4}}
# {3: {1, 0},
# 1: {0}}


# query the dict for both
# iterate over the pairs
# check if the second val is in dict
# if its already there, then add first val to the set
# if its not already there, then create entry with second value at set

# grab the values for passed in ints
# check if there is an intersection
# return true if there is


def hasCommonAncestor(parent_child_pairs, int1, int2):
    dictionary = {}
    for pair in parent_child_pairs:
        if pair[0] not in dictionary:
            dictionary[pair[0]] = set()

        if pair[1] in dictionary:
            # adding child
            dictionary[pair[1]].add(pair[0])
        else:
            # adding child
            dictionary[pair[1]] = {pair[0]}

        # checking for other ancestors
        if pair[0] in dictionary:
            for value in dictionary[pair[0]]:
                dictionary[pair[1]].add(value)

    for key, value in dictionary.items():
        for item in value:
            if item in dictionary:
                ancestors = dictionary[item]
                for x in ancestors:
                    value.


print(hasCommonAncestor(parent_child_pairs_1, 3, 8))


# def findNodesWithZeroAndOneParents(parent_child_pairs):
#     # n = number of nodes
#     #

#     histogram = {}
#     for pair in parent_child_pairs:
#         if pair[0] not in histogram.keys():
#             # add with count = 0
#             histogram[pair[0]] = 0

#         if pair[1] not in histogram.keys():
#             histogram[pair[1]] = 1
#         else:
#             histogram[pair[1]] += 1

#     results = [[],[]]
#     for key, value in histogram.items():
#         # print(value)
#         if value == 0:
#             results[0].append(key)
#         elif value == 1:
#             results[1].append(key)

#     return results
