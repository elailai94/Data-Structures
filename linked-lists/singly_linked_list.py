class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = f'Value: {self.value}, Next: '

        if self.next is None:
            string += 'None'
        else:
            string += '->'

        return string

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __getitem__(self, index):
        """
        Access the value at the given index in the linked list.

        Time complexity: O(n) where n is the number of nodes in the linked list.
        """
        current_index = 0
        current_node = self.head

        while (current_index <= index and current_node is not None):
            if current_index == index:
                return current_node.value
            current_index += 1
            current_node = current_node.next

        raise IndexError(f'linked list index {index} out of range')

    def __len__(self):
        """
        Return the length (i.e.: number of nodes) in the linked list.
        
        Time complexity: O(n) where n is the number of nodes in the linked list.
        """
        length = 0
        current_node = self.head
        
        while current_node is not None:
            length += 1
            current_node = current_node.next

        return length
    
    def __str__(self):
        """
        Return the string representation of the linked list.

        Time complexity: O(n) where n is the number of nodes in the linked list.
        """
        string = ''
        current_node = self.head

        while current_node is not None:
            string += str(current_node)
            if current_node.next is not None:
                string += ' '
            current_node = current_node.next

        return string

    def append(self, value):
        """
        Add a value to the end of the linked list.
        
        Time complexity: O(n) where n is the number of nodes in the linked list.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert(self, index, value):
        """
        Insert a value at the given index in the linked list.

        Time complexity: O(n) where n is the number of nodes in the linked list.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            elif index > 0:
                current_index = 0
                current_node = self.head
                
                while (current_index < index and current_node is not None):
                    if current_index == index - 1:
                        new_node.next = current_node.next
                        current_node.next = new_node
                        return
                    current_index += 1
                    current_node = current_node.next
                
                self.append(value)

    def remove(self, value):
        """
        Remove a value from the linked list.

        Time complexity: O(n) where n is the number of nodes in the linked list.
        """
        error_message = f'linkedlist.remove({value}) {value} not in linked list'

        if self.head is None:
            raise ValueError(error_message)
        else:
            previous_node = None
            current_node = self.head
            
            while (current_node.value != value and
                current_node.next is not None):
                previous_node = current_node
                current_node = current_node.next
            
            if current_node.value == value:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
            else:
                raise ValueError(error_message)
