class Node:
    def __init__(self, n):
        self.data = n
        self.next = None
        self.prev = None

class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addback(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
    
    def swap_pairs(self):
        current = self.head
        while current and current.next:
            current.data, current.next.data = current.next.data, current.data
            current = current.next.next
l = dll()
l.addback(5)
l.addback(7)
l.addback(8)
l.addback(2)
l.addback(1)
l.addback(4)

print("Original list:")
l.display()
l.swap_pairs()

print("Swapped list:")
l.display()
