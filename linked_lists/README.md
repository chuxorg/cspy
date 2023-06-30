# Linked Lists

A linked list is a linear data structure where each element is a separate object known as a node. Each node contains two fields: "data" and "next". The "data" field stores any kind of data, such as a number, a string, or any other type of object. The "next" field is a pointer that links one node to another, forming a chain.

There are several types of linked lists, but the simplest one is the singly linked list. In a singly linked list, each node points to the next node in the list, and the last node points to None (indicating the end of the list). The list itself can be referenced by a single external pointer, the "head", which points to the first node in the list.

Here's a simple implementation of a singly linked list in Python:

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            
    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        print(" -> ".join(str(value) for value in values))
```

You can use the LinkedList like this:

```python
linked_list = LinkedList()
linked_list.append('Python')
linked_list.append('is')
linked_list.append('great!')
linked_list.display()
```

Output:
```
Python -> is -> great!
```

Unlike arrays or lists in Python, linked lists are dynamic and allocate the needed memory while running, not in advance. This makes them efficient for use-cases where the size of the list isn't known in advance.

However, access time for a particular element isn't constant as in arrays - you need to traverse the list from the head node to get to the desired node, which can be time-consuming. 

So while linked lists have their use-cases, in Python, you would typically use the built-in list or deque (double-ended queue) data structures for most purposes where you might use a linked list in lower-level languages. These Python data structures provide the benefits of linked lists, like dynamic sizing, but also offer many other benefits, like constant-time access to elements, due to the specifics of their implementation.