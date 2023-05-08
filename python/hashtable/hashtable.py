class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def display(self):
        collection = []
        current = self
        while current:
            if current.value is not None:
                collection.append([current.key, current.value])
            current = current.next
        return collection


class Hashtable:
    def __init__(self, size=1064):
        self._size = size
        self._buckets = [None] * self._size

    def _hash(self, key):
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        prime = hash_sum * 599
        return prime % self._size

    def set(self, key, value):
        index = self._hash(key)
        if not self._buckets[index]:
            self._buckets[index] = Node(key, value)
        else:
            current = self._buckets[index]
            while True:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self._buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def keys(self):
        keys = []
        for bucket in self._buckets:
            if bucket:
                current = bucket
                while current:
                    keys.append(current.key)
                    current = current.next
        return keys

    def has(self, key):
        index = self._hash(key)
        current = self._buckets[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False
