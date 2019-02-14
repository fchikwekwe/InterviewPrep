"""
Implement a stack with the following methods:
push: puts an item on top of  stack
pop: removes an element from top of stack
peek: returns the top element on the stack
is_empty: returns true is elements are not in the stack, else, returns false
"""
# stacks are FILO
# we need to add to the same end that we remove from
# The top of the stack will be the end (highest index)

class Stack:
    def __init__(self):
        """
        Store the stack in a Python list.
        """
        self.items = []

    def is_empty(self):
        """
        Returns true if there are no elements in the stack.
        Otherwise, returns false.
        Time complexity: O(1)
        """
        if self.items == []:
            return True
        return False

    def push(self, new_item):
        """
        Adds an element to the top of the stack.
        Time complexity: O(1)
        """
        self.items.append(new_item)

    def pop(self):
        """
        Removes and returns the top element from the stack.
        Time complexity: O(1)
        """
        return self.items.pop()

    def peek(self):
        """
        Looks at the stack and returns the top item.
        """
        top_item = len(self.items) - 1 # highest index in stack
        return self.items[top_item]


class StackMax:
    """
    Implement a stack with the following methods:
    Push, pop, peek, is_empty and max.
    """
    def __init__(self):
        """
        Keep track of items in stack.
        Keep track of max values in order they were put into the stack.
        """
        self.items = []
        self.max = []

    def is_empty(self):
        """
        Checks to see if self.items is empty.
        Returns True if self.items is empty (has no values).
        Return False if there are any values in self.items.
        """
        if self.items == []:
            return True
        return False

    def pop(self):
        """
        First, checks to see if self.items has any values.
        Then, removes top item from the stack.
        """
        if self.is_empty:
            raise IndexError
        else:
            if self.items[-1] == self.max[-1]:
                self.max.pop()
                return self.items.pop()
            else:
                return self.items.pop()

    def push(self, new_item):
        """
        First, checks to see if there are any stored max values to compare with.
        Then, compares new item with top item in max to see which if it is greater than or equal to.
        Depending on which cases are true, either appends to max and items or just items.
        """
        if self.max == []: # check if max list is empty
            self.max.append(new_item)
            self.items.append(new_item)
        else:
            if new_item >= self.max[-1]: # checks if new item is greater or equal to top item in max
                self.max.append(new_item)
                self.items.append(new_item)
            else:
                self.items.append(new_item)

    def max(self):
        """
        Checks to see if max list is empty.
        If not, then it returns the top item from max list.
        """
        if self.max == []:
            return None
        return self.max[-1]


class Node:
    def __init__(self):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def push(self, new_item):
        top = Node(new_item)
        self.top.next = self.head
        self.head = self.top

    def pop(self):
        pop_value = self.head
        self.head = self.head.next
        return pop_value # if there is no head, this returns None

    def peek(self):
        return self.head # if there is no head, this returns None

    def max(self):
        pass
