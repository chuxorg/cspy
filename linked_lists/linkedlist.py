class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
    
    def pop(self):
        """
        Pop is a little less straightforward than the other methods.
        The objective is to remove the last node of the Linked List.'
        To accomplish this, we will use to variables to track where we are
        Returns:
            _type_: _description_
        """
        if self.head is None:
            return None
        else:
            return self.head.value  
    
    def append(self, value):
        """
           Puts a new node at the end of the Linked List. Time complexity O(n) 
        Args:
            value (Object): This will be a value of any type 
        """
        # Create a new node with the value
        node = Node(value)
        # If there's no head, create one
        if self.head is None:
            # This condition is when the Linked List is empty
            # Set the head and tail to the new node
            self.head = node 
            self.tail = node
        else:
            # Appending means to add to the end of the linked list.
            # Here we set the next node of the current tail to the new node
            self.tail.next = node
            self.tail = node
        
        # Increment the length of the Linked List by one
        self.length += 1
        
        # 
        return True 
    
    def prepend(self, value):
        """
            Puts a new node at the beginning of the Linked List        
        Args:
            value (Object): This will be a value of any type
        """
        if self.head is None:
            # This conditional is not necessary, but just in case.
            self.head = Node(value)
            return
        # Create a new node with the value and set it as the head node
        node = Node(value)
        # Set the next node of the new node to the current head node
        node.next = self.head
        #  Now the new node is the head node
        self.head = node
        return
    
    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        node = self.head
        for i in range(index-1):
            node = node.next
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        return
    
    def print_list(self):
        """
        Prints all the values of the Linked List. Complexity O(n)
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def __repr__(self):
        """ 
            Returns a string representation of the Linked List. Complexity O(n)
        Returns:
            string: A string representation of the Linked List
        """
        node = self.head
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next
        return f"{nodes}"
    def __len__(self):
        return self.length