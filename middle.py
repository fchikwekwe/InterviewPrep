#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) because the item is always
        inserted at the end of list. """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.size == 0:
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
        # update size property
        self.size += 1
        # Update tail to new node regardless
        self.tail = new_node

    def middle(self):
        """
        Clarified with interviewer: 
        - If self.size is 0, then return None 
        - If there is one middle value, return just data
        - If there are two middle values, return tuple with data
        """
        if self.size == 0:
            # Linked List is empty
            return None

        even = False
        if self.size % 2 == 0: # even
            mid_ind = self.size / 2
            even = True
        else:
            mid_ind = (self.size // 2) + 1

        counter = 1
        node = self.head

        # traverse until you arrive at middle node
        while counter != mid_ind:
            counter += 1
            node = node.next

        if even:  # two middle values
            first = node.data
            second = node.next.data
            return (first, second)

        # if size is not even, there is one middle value
        return node.data


def test_linked_list():
    ll = LinkedList(['A', 'B', 'C', ])
    print(ll)
    ll_2 = LinkedList([1, 2, 3, 4])
    ll_3 = LinkedList()
    print('Testing middle method:')
    print(ll.middle())
    print(ll_2.middle())
    print(ll_3.middle())



if __name__ == '__main__':
    test_linked_list()
