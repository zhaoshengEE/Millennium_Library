"""
Q1. Add a method to print all the elements of the linked list
Q3. Add a method to return the last element of the linked list. Assume we don't know the number of elements in the list.
Q4. Reverse the Linked list
"""

# Adpated from https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class LinkedList:
    def __init__(self):
       self.head = None
    
    def printAll(self):
        self.current = self.head
        while self.current is not None:
            print(self.current.data)
            self.current = self.current.next

    def fetchLastNode(self):
        self.current = self.head
        while self.current.next is not None:
            self.current = self.current.next
        return self.current.data

    def reverseLinkedList(self):  
        self.previous = None
        self.current = self.head
        while self.current is not None:
            self.temp = self.current.next
            self.current.next = self.previous
            self.previous = self.current
            self.current = self.temp
        self.head = self.previous

if __name__ == "__main__":
    list1 = LinkedList()
    list1.head = Node("A")
    e2 = Node("B")
    e3 = Node("C")
    # Link first Node to second node
    list1.head.next = e2

    # Link second Node to third node
    e2.next = e3

    list1.printAll()

    lastNode = list1.fetchLastNode()
    print(lastNode)

    list1.reverseLinkedList()
    list1.printAll()