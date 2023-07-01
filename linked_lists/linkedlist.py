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
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = Node(value)
        node.next = self.head
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