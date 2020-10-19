# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:
    data = []

    def __init__(self, size=10):
        self.size = size
        for x in range(0,self.size):
            self.data.append([])

    def __getitem__(self, item):
        print('test')
        print(self.hash(item))
        if(self.data[self.hash(item)] == []):
            return None

        key = self.hash(item) % self.size
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[self.hash(key)] = [[key,value]]

    def hash(self, key):
        out = None
        if(type(key) == str):
            out = hash(key)
        else:
            out = key

        return out % self.size

    pass
