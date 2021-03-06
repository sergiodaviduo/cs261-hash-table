# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:
    data = []
    key_list = []
    value_list = []

    def __init__(self, size=10):
        self.size = size
        for x in range(0,self.size):
            self.data.append([])

    def __getitem__(self, item):
        print('testget')
        print(self.hash(item))
        if(self.data[self.hash(item)] == []):
            return None

        key = self.hash(item)
        ret = self.data[key]
        ret1 = ret[0]
        ret2 = ret1[1]
        return ret2

    def __setitem__(self, key, value):
        if(self.data[self.hash(key)] == []):
            self.data[self.hash(key)] = [[key, value]]
            self.key_list.append(key)
            self.value_list.append(value)
        else:
            self.data[self.hash(key)].append([key, value])
            self.key_list.append(key)
            self.value_list.append(value)

    def hash(self, key):
        out = None
        if(type(key) == str):
            out = hash(key)
        else:
            out = key

        return out % self.size

    def delete(self, instance):
        if (self.data[self.hash(instance)] == []):
            return None
        key = self.hash(instance)
        self.data[key] = []

    def clear(self):
        for x in range(0,self.size):
            self.data[x] = []

    def keys(self):
        return self.key_list

    def values(self):
        return self.value_list
    pass
