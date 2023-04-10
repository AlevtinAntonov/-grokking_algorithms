class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def append(self, val):
        end = Node(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end

ll = Node(1)
ll.append(2)
ll.append(3)

node = ll
print(node.data)
while node.next:
    node = node.next
    print(node.data)