# =============================================================================
#  Singly Linked List
#
#  @author: Elisha Lai
#  @description: Module for implementing a singly linked list.
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
            next = '→'
        
        return f'Value: {self.value}, Next: {next}'

class SinglyLinkedList:
    def __init__(self, head=None):
        """
        Create a new instance of a linked list.

        Time: O(1)
        """
        self.head = head

    def __getitem__(self, index):
        """
        Access the value at the given index in the linked list.

        Time: O(n) where n is the number of nodes in the linked list.
        """
        current_index = 0
        current_node = self.head

        while current_index <= index and current_node:
            if current_index == index:
                return current_node.value

            current_index += 1
            current_node = current_node.next

        raise IndexError(f'linked list index {index} out of range')

    def __len__(self):
        """
        Return the length (i.e.: number of nodes) of the linked list.

        Time: O(n) where n is the number of nodes in the linked list.
        """
        length = 0
        current_node = self.head
        
        while current_node:
            length += 1
            current_node = current_node.next

        return length
    
    def __str__(self):
        """
        Return the string representation of the linked list.

        Time: O(n) where n is the number of nodes in the linked list.
        """
        string = ''
        current_node = self.head

        while current_node:
            string += str(current_node)

            if current_node.next:
                string += ' '

            current_node = current_node.next

        return string

    def append(self, value):
        """
        Add a value to the end of the linked list.

        Time: O(n) where n is the number of nodes in the linked list.
        """
        new_node = Node(value)

        if self.head:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
        else:
            self.head = new_node

    def insert(self, index, value):
        """
        Insert a value at the given index in the linked list.

        Time: O(n) where n is the number of nodes in the linked list.
        """
        new_node = Node(value)

        if self.head:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            elif index > 0:
                current_index = 0
                current_node = self.head

                while current_index < index and current_node:
                    if current_index == index - 1:
                        new_node.next = current_node.next
                        current_node.next = new_node

                        return

                    current_index += 1
                    current_node = current_node.next

                self.append(value)
        else:
            self.head = new_node

    def remove(self, value):
        """
        Remove a value from the linked list.

        Time: O(n) where n is the number of nodes in the linked list.
        """
        error_message = f'linkedlist.remove({value}) {value} not in linked list'

        if self.head:
            previous_node = None
            current_node = self.head

            while current_node.value != value and current_node.next:
                previous_node = current_node
                current_node = current_node.next

            if current_node.value == value:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
            else:
                raise ValueError(error_message)
        else:
            raise ValueError(error_message)
