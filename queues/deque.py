# =============================================================================
#  Deque
#
#  @author: Elisha Lai
#  @description: Module for implementing a deque using a doubly linked list.
#  @version: 0.0.1 23/02/2019
# =============================================================================

class Node:
    def __init__(self, value, previous=None, next=None):
        """
        Create a new instance of a node.

        Time: O(1)
        """
        self.value = value
        self.previous = previous
        self.next = next

    def __str__(self):
        """
        Return the string representation of the node.

        Time: O(1)
        """
        previous = 'None'
        next = 'None'

        if self.previous:
            previous = '←'

        if self.next:
            next = '→'

        return f'Previous: {previous}, Value: {self.value}, Next: {next}'

class Deque:
    def __init__(self, head=None, tail=None):
        """
        Create a new instance of a deque.

        Time: O(1)
        """
        self.head = head
        self.tail = tail

    def __len__(self):
        """
        Return the length (i.e.: number of nodes) of the deque.

        Time: O(n) where n is the number of nodes in the deque.
        """
        length = 0
        current_node = self.head

        while current_node:
            length += 1
            current_node = current_node.next

        return length

    def __str__(self):
        """
        Return the string representation of the deque.

        Time: O(n) where n is the number of nodes in the deque.
        """
        string = ''
        current_node = self.head

        while current_node:
            string += str(current_node)

            if current_node.next:
                string += ' '

            current_node = current_node.next

        return string

    def dequeue_back(self):
        """
        Remove and return the value from the tail of the deque.

        Time: O(1)
        """
        if self.tail:
            value = self.tail.value

            if self.tail.previous:
                self.tail.previous.next = None

            self.tail = self.tail.previous

            if not self.tail:
                self.head = self.tail

            return value
        else:
            raise IndexError('dequeue back from empty deque')

    def dequeue_front(self):
        """
        Remove and return the value from the head of the deque.

        Time: O(1)
        """
        if self.head:
            value = self.head.value

            if self.head.next:
                self.head.next.previous = None

            self.head = self.head.next

            if not self.head:
                self.tail = self.head

            return value
        else:
            raise IndexError('dequeue front from empty deque')

    def enqueue_back(self, value):
        """
        Add a value to the tail of the deque.

        Time: O(1)
        """
        new_node = Node(value, self.tail)

        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def enqueue_front(self, value):
        """
        Add a value to the head of the deque.

        Time: O(1)
        """
        new_node = Node(value, None, self.head)

        if self.head:
            self.head.previous = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
