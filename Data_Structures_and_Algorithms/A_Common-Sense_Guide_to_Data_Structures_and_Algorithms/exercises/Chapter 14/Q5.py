"""

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
    
    def removeSpecificNode(self, node):
        self.current = node
        while True:
            self.previous = self.current
            self.current = self.current.next
            self.previous.data, self.current.data = self.current.data, self.previous.data
            if self.current.next is None:
                self.previous.next = None
                break
            else:
                self.previous = self.current
                self.current = self.current.next
            
if __name__ == "__main__":
    list1 = LinkedList()
    list1.head = Node("A")
    e2 = Node("B")
    e3 = Node("C")
    # Link first Node to second node
    list1.head.next = e2

    # Link second Node to third node
    e2.next = e3
    list1.removeSpecificNode(e2)
    list1.printAll()