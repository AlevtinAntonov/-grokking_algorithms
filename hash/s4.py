class HashTable:
    def __init__(self, size=None):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def hash_func(self, key, size):
        return key % size

    def insert_data(self, key, data):
        index = self.hash_func(key, self.size)
        self.slots[index] = key
        self.data[index] = data

    def get_data(self, key):
        index = self.hash_func(key, self.size)
        return self.data[index]

    def print_hash(self):
        print(list(zip(self.slots, self.data)))


table = HashTable(10)
table.insert_data(1, "a")
table.insert_data(11, "hello")
table.insert_data(2, "b")
print(table.get_data(21))
table.print_hash()
