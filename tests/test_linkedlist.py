import unittest

from .context import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_append(self):
        linked_list = LinkedList(10)
        linked_list.append(20)
        linked_list.append(30)
        self.assertEqual(linked_list.head.value, 10)
        self.assertEqual(linked_list.head.next.value, 20)
        self.assertEqual(linked_list.head.next.next.value, 30)
        self.assertIsNone(linked_list.head.next.next.next)

    def test_prepend(self):
        linked_list = LinkedList(10)
        linked_list.prepend(5)
        linked_list.prepend(1)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.head.next.value, 5)
        self.assertEqual(linked_list.head.next.next.value, 10)
        self.assertIsNone(linked_list.head.next.next.next)

    def test_insert(self):
        linked_list = LinkedList(10)
        linked_list.append(20)
        linked_list.append(30)
        linked_list.insert(1, 15)
        self.assertEqual(linked_list.head.value, 10)
        self.assertEqual(linked_list.head.next.value, 15)
        self.assertEqual(linked_list.head.next.next.value, 20)
        self.assertEqual(linked_list.head.next.next.next.value, 30)
        self.assertIsNone(linked_list.head.next.next.next.next)

if __name__ == '__main__':
    unittest.main()
