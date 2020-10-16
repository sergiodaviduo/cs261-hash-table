# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:
    data = []

    def __init__(self, size=10):
        self.size = size

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data.append({key: value})

    pass
