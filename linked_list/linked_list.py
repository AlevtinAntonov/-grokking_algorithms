class Node:
    def __init__(self, node=None):
        self.node = node
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, value):
        last_node = self.head
        while last_node:
            if value == last_node.node:
                return True
            else:
                last_node = last_node.next_node
        return False

    def addToEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    # def get(self, catIndex):
    #     lastbox = self.head
    #     boxIndex = 0
    #     while boxIndex <= catIndex:
    #         if boxIndex == catIndex:
    #             return lastbox.node
    #         boxIndex = boxIndex + 1
    #         lastbox = lastbox.next_node

    def removeNode(self, rmnode):
        head = self.head

        if head is not None:
            if head.node == rmnode:
                self.head = head.next_node
                head = None
                return
        while head is not None:
            if head.node == rmnode:
                break
            last_node = head
            head = head.next_node
        if head == None:
            return
        last_node.next_node = head.next_node
        head = None

    def LLprint(self):
        current_node = self.head
        print("LINKED LIST")
        print("-----")
        i = 0
        while current_node is not None:
            print(str(i) + ": " + str(current_node.node))
            i += 1
            current_node = current_node.next_node
        print("-----")

    def reversedList(self):
        # current = head
        # new_head = None
        # while current:
        #     data = Node(current.node)
        #     head.next_node, head, new_head = new_head, head.next_node, head
        # return new_head
        current = self.head
        new_head = None

        while current:
            node = Node(current.node)

            # Assign the new head to node's next
            node.next_node = new_head

            # Assign the node to new head
            new_head = node
            current = current.next_node

        return new_head


linkedlist = LinkedList()
linkedlist.addToEnd('One')
linkedlist.addToEnd('2')
linkedlist.addToEnd('Three')
linkedlist.addToEnd(4)
linkedlist.LLprint()

linkedlist.removeNode('2')

linkedlist.LLprint()
linkedlist.reversedList()
linkedlist.LLprint()

# print(linkedlist.get(0))
