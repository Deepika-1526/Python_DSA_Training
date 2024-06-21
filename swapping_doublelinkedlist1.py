class Node:
    def __init__(self, n):
        self.data = n
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_back(self, x):
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
            next_pair = current.next.next
            first = current
            second = current.next
            if first.prev:
                first.prev.next = second
            else:
                self.head = second 
            
            second.prev = first.prev
            first.prev = second
            first.next = second.next
            second.next = first
            if first.next:
                first.next.prev = first
            else:
                self.tail = first  
            current = next_pair
l = DLL()
l.add_back(5)
l.add_back(7)
l.add_back(8)
l.add_back(2)
l.add_back(1)
l.add_back(4)

print("Original list:")
l.display()
l.swap_pairs()

print("Swapped list:")
l.display()
