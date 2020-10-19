# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:
    data = []

    def __init__(self, size=10):
        self.size = size
        for x in range(0,self.size):
            self.data.append(None)

    def __getitem__(self, item):
        return self.hash(item)

    def __setitem__(self, key, value):
        self.data.append(hash(key),value)

    def hash(self, key):
        out = None
        if(type(key) == str):
            out = hash(key)
        else:
            out = key

        return out % self.size

    pass
