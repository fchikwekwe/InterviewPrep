
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def array_insert(heap, node):
    heap.append(node)
    index = len(heap) - 1
    parent_index = (index - 1) // 2
    parent = heap[parent_index]

    while node < parent: 
        # switch parent and child values
        heap[parent_index] = node # put node at parent value
        heap[index] = parent
        
        # reassign get new node index 
        index = parent_index 

        # calculate new parent index and get parent
        parent_index = (index - 1) // 2
        parent = heap[parent_index]
    return heap

example_heap = [3, 4, 10, 13, 15, 11, 12, 15, 20, 16, 17]
print(array_insert(example_heap, 5))
