class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        """
        Return the string representation of the node.

        Time: O(1)
        """
        string = f'Value: {self.value}, Next: '

        if self.next:
            string += '↓'
        else:
            string += 'None'

        return string

class Stack:
    def __init__(self, top=None):
        self.top = top

    def __len__(self):
        """
        Return the length (i.e.: number of nodes) in the stack.

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
            raise IndexError('peek from empty list')

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
            raise IndexError('pop from empty list')

    def push(self, value):
        """
        Add a value to the top of the stack.

        Time: O(1)
        """
        new_node = Node(value, self.top)
        self.top = new_node
