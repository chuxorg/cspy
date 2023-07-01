# Linked Lists

Author: Chuck Sailer

A linked list is a linear data structure where each element is a separate object known as a node. Each node contains two fields: "data" and "next". The "data" field stores any kind of data, such as a number, a string, or any other type of object. The "next" field is a pointer that links one node to another, forming a chain.

There are several types of linked lists, but the simplest one is the singly linked list. In a singly linked list, each node points to the next node in the list, and the last node points to None (indicating the end of the list). The list itself can be referenced by a single external pointer, the "head", which points to the first node in the list.

Here's a simple implementation of a singly linked list in Python:

```python
# The Node class represents a node in the linked list. It will contain a value and a pointer, called next, to the
# next node in the list.
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
            # Set the head node as current
            current = self.head
            while current.next:
                # traverse the linked list while the current node's 
                # next value is not None.
                current = current.next
            # We've reached the end of the Linked List. Create a new Node
            # and set it to the 'next' value of the current node.
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

There are several benefits to the way linked lists store values in random, non-contiguous blocks of memory:

1. Dynamic Size: Linked lists allow for dynamic resizing. As elements are added or removed from a linked list, memory can be allocated or deallocated as needed. This flexibility is particularly useful when the size of the data structure needs to change frequently.

2. Efficient Insertions and Deletions: Insertions and deletions at arbitrary positions within a linked list can be performed with a time complexity of O(1) as long as the position is known. This is because adding or removing a node in a linked list only requires updating a few pointers, whereas in an array, it may involve shifting or copying a large number of elements.

3. Memory Efficiency: Linked lists do not require a contiguous block of memory. Each node in a linked list contains a reference or pointer to the next node, allowing the list to be constructed using scattered memory locations. This can be beneficial when dealing with large datasets or when memory is fragmented.

4. Easy to Insert and Delete at the Head: Linked lists make it easy and efficient to insert or delete elements at the beginning of the list. Since the head of the list is just a pointer, inserting or deleting a node at the head simply involves updating the pointer, which has a time complexity of O(1). In contrast, inserting or deleting elements at the beginning of an array requires shifting or copying all the elements, resulting in a time complexity of O(n).

5. Versatility: Linked lists can be used to implement various data structures, such as stacks, queues, and hash tables. The ability to easily insert and delete elements makes linked lists a suitable choice for these dynamic data structures.

Despite these advantages, linked lists also have some drawbacks. They generally require more memory per element due to the additional pointers, and accessing elements at arbitrary positions has a time complexity of O(n), as you need to traverse the list from the beginning or end. Arrays, on the other hand, provide constant-time access to elements using indices. Therefore, the choice between linked lists and arrays depends on the specific requirements and constraints of the problem at hand.

So while linked lists have their use-cases, in Python, you would typically use the built-in list or deque (double-ended queue) data structures for most purposes where you might use a linked list in lower-level languages. These Python data structures provide the benefits of linked lists, like dynamic sizing, but also offer many other benefits, like constant-time, O(1), access to elements, due to the specifics of their implementation.