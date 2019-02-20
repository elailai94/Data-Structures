# =============================================================================
#  Queue
#
#  @author: Elisha Lai
#  @description: Module for implementing a queue using a singly linked list.
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
        string = f'Value: {self.value}, Next: '

        if self.next:
            string += '→'
        else:
            string += 'None'

        return string

class Queue:
    def __init__(self, head=None, tail=None):
        """
        Create a new instance of a queue.

        Time: O(1)
        """
        self.head = head
        self.tail = tail
    
    def __len__(self):
        """
        Return the length (i.e.: number of nodes) of the queue.

        Time: O(n) where n is the number of nodes in the queue.
        """
        length = 0
        current_node = self.head

        while current_node:
            length += 1
            current_node = current_node.next

        return length

    def __str__(self):
        """
        Return the string representation of the queue.

        Time: O(n) where n is the number of nodes in the queue.
        """
        string = ''
        current_node = self.head

        while current_node:
            string += str(current_node)
            if current_node.next:
                string += ' '
            current_node = current_node.next

        return string

    def dequeue(self):
        """
        Remove and return the value from the head of the queue.

        Time: O(1)
        """
        if self.head:
            value = self.head.value
            self.head = self.head.next
            if not self.head:
                self.tail = self.head
            return value
        else:
            raise IndexError('dequeue from empty queue')

    def enqueue(self, value):
        """
        Add a value to the tail of the queue.

        Time: O(1)
        """
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
