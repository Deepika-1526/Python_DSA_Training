class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def sums(self, node, even_sum=0, odd_sum=0):
        if node is None:
            return even_sum, odd_sum
        if node.data % 2 == 0:
            even_sum += node.data
        else:
            odd_sum += node.data
        return self.sums(node.next, even_sum, odd_sum)

def main():
    dll = DoublyLinkedList()
    elements = [1, 2, 3, 4, 5, 6]
    for elem in elements:
        dll.append(elem)
    
    even_sum, odd_sum = dll.sums(dll.head)
    result = abs(even_sum - odd_sum)
    print(result)
main()
