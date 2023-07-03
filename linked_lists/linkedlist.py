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
        
    
    def append(self, value):
        """
           Puts a new node at the end of the Linked List. Time complexity O(n) 
        Args:
            value (Object): This will be a value of any type 
        """
        # If there's no head, create one
        if self.head is None:
            # This conditional is not necessary, but just in case.
            # The head is set in the constructor
            self.head = Node(value)
            return
        # If there is a head, copy it to a variable
        node = self.head
        while node.next:
            # iterating over all nodes in the list looking for the last one 
            # (Node with next -> None is the last node)
            node = node.next
        # Create a new node with the value amd set it as the next node of the last node
        # Remember that the node variable is a pointer to self.head. Now, we are giving the head node
        # a new next node, which is the new node we just created    
        node.next = Node(value)
        return
    
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