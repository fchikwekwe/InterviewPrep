""" Implement a binary search tree from scratch """

class Node(object):
    """ inherits from Python object class
        attributes: data, right, left """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    """ inherits from Python object class """
    def __init__(self):
        self.root = None

    def add(self, data):
        new_node = Node(data)
        # self.root = 5
        # new_node = 3
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            previous_node = None
            # keep running loop until current node is none
            while current_node is not None:
                # keep track of previous pointer
                previous_node = current_node
                # if new node is less than; move left
                if current_node.data >= new_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
                # if new node is greater than; move right
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node.right = new_node
