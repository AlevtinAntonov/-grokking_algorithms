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

ll = Node(100)
ll.append(200)
ll.append(300)

node = ll
print(node.data)
while node.next:
    node = node.next
    print(node.data)