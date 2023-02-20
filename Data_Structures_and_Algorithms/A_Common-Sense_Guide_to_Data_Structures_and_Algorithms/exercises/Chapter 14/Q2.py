"""
Print all the elements of a doubly linked list in reverse order.
"""

# Adapted from https://favtutor.com/blogs/doubly-linked-list-python#:~:text=A%20doubly%20linked%20list%20has,next%20node%20in%20the%20sequence.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def reversePrint(self):
        self.current = self.tail
        while self.current is not None:
            print(self.current.data)
            self.current = self.current.previous

if __name__ == "__main__":
    list1 = doublyLinkedList()
    list1.head = Node("A")
    e2 = Node("B")
    e3 = Node("C")
    list1.tail = e3

    list1.head.next = e2

    e2.next = e3
    e2.previous = list1.head

    e3.previous = e2

    list1.reversePrint()