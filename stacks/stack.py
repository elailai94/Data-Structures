# =============================================================================
#  Stack
#
#  @author: Elisha Lai
#  @description: Module for implementing a stack using a singly linked list.
#  @version: 0.0.1 19/02/2019
# =============================================================================

class Node:
    def __init__(self, value, next=None):
        """
        Create a new instance of a node.

        Time: O(1)
        """
        self.value = value
        self.next = next

    def __str__(self):
        """
        Return the string representation of the node.

        Time: O(1)
        """
        next = 'None'

        if self.next:
            next = '↓'
        
        return f'Value: {self.value}, Next: {next}'

class Stack:
    def __init__(self, top=None):
        """
        Create a new instance of a stack.

        Time: O(1)
        """
        self.top = top

    def __len__(self):
        """
        Return the height (i.e.: number of nodes) of the stack.

        Time: O(n) where n is the number of nodes in the stack.
        """
        length = 0
        current_node = self.top

        while current_node:
            length += 1
            current_node = current_node.next

        return length

    def __str__(self):
        """
        Return the string representation of the stack.

        Time: O(n) where n is the number of nodes in the stack.
        """
        string = ''
        current_node = self.top

        while current_node:
            string += str(current_node)

            if current_node.next:
                string += '\n'

            current_node = current_node.next

        return string

    def peek(self):
        """
        Return the value from the top of the stack without removing it.

        Time: O(1)
        """
        if self.top:
            return self.top.value
        else:
            raise IndexError('peek from empty stack')

    def pop(self):
        """
        Remove and return the value from the top of the stack.

        Time: O(1)
        """
        if self.top:
            value = self.top.value
            self.top = self.top.next

            return value
        else:
            raise IndexError('pop from empty stack')

    def push(self, value):
        """
        Add a value to the top of the stack.

        Time: O(1)
        """
        new_node = Node(value, self.top)
        self.top = new_node
