class Box:
    def __init__(self, cat = None):
        self.cat = cat
        self.next_cat = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def contains(self, cat):
        last_box = self.head
        while last_box:
            if cat == last_box.node:
                return True
            else:
                last_box = last_box.next_cat
        return False

    def add_to_end(self, new_cat):
        new_box = Box(new_cat)
        if self.head is None:
            self.head = new_box
            return
        last_box = self.head
        while last_box.next_cat:
            last_box = last_box.next_cat
        last_box.next_cat = new_box

    def get(self, cat_index):
        last_box = self.head
        box_index = 0
        while box_index <= cat_index:
            if box_index == cat_index:
                return last_box.node
            box_index = box_index + 1
            last_box = last_box.next_cat

    def remove_box(self, rm_cat):
        head_cat = self.head

        if head_cat is not None:
            if head_cat.node == rm_cat:
                self.head = head_cat.next_cat
                head_cat = None
                return
        while head_cat is not None:
            if head_cat.node == rm_cat:
                break
            last_cat = head_cat
            head_cat = head_cat.next_cat
        if head_cat == None:
            return
        last_cat.next_cat = head_cat.next_cat
        head_cat = None

    def llprint(self):
        current_cat = self.head
        print("LINKED LIST")
        print("-----")
        i = 0
        while current_cat is not None:
            print(str(i) + ": " + str(current_cat.node))
            i += 1
            current_cat = current_cat.next_cat
        print("-----")


linked_list = LinkedList()
linked_list.add_to_end('One')
linked_list.add_to_end('Two')
linked_list.add_to_end('Five-Three')
linked_list.add_to_end(3)
linked_list.add_to_end(4.5)
linked_list.llprint()

linked_list.remove_box('Five-Three')
linked_list.llprint()

print(linked_list.get(1))


         