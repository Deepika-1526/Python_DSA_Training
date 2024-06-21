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

    def is_prime(self, num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def count_primes(self, node):
        if node is None:
            return 0
        if self.is_prime(node.data):
            return 1 + self.count_primes(node.next)
        else:
            return 0 + self.count_primes(node.next)

def main():
    dll = DoublyLinkedList()
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for elem in elements:
        dll.append(elem)
    
    prime_count = dll.count_primes(dll.head)
    print(prime_count)
main()
