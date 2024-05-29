from typing import Optional

from misc.bloom_filter import BloomFilter


class Node:
    # Node class for linked list
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    # Basic linked list class
    def __init__(self):
        self.head = None


    def add(self, key, value):
        """
        Add a new node to the linked list
        """

        # If the linked list is empty, add the node as the head
        if self.head is None:
            self.head = Node(key, value)
        else:
            # Traverse the linked list from head to find the last node
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = Node(key, value)

    def get(self, key):
        cursor = self.head
        while cursor is not None:
            if cursor.key == key:
                return cursor.value
            cursor = cursor.next
        return None

    def get_by_value(self, value):
        cursor = self.head
        while cursor is not None:
            if cursor.value == value:
                return cursor.key
            cursor = cursor.next
        return None

    def remove(self, key):
        # If the linked list is empty, return
        if self.head is None:
            return
        
        # If the head is the node to be removed
        if self.head.key == key:
            self.head = self.head.next
            return
        
        # Traverse the linked list to find the node to be removed
        cursor = self.head
        while cursor.next is not None:
            if cursor.next.key == key:
                cursor.next = cursor.next.next
                return
            cursor = cursor.next

class HashTable:
    # Hash table class
    def __init__(self, size: Optional[int] = None):
        # This is optional but we can specify the size
        self.size = size
        # The table itself is an array of linked lists
        self.table = [LinkedList() for _ in range(size)]
        self.filter = BloomFilter()

    def _hash(self, key):
        return hash(key) % self.size if self.size else hash(key) % len(self.table)

    def add(self, key, value):
        # When we add an attribute to the hash table, we get the index by first finding the hash key
        index = self._hash(key)
        # Then at that index we add it to the linked list
        # If we want to utilize the Bloom Filter, we can add the key to the Bloom Filter here
        # the filter has the key
        if self.filter.contains(key):
            # then try to rehash and find a different key
            self.add(key + "1", value)
        else:
            self.table[index].add(key, value)

    def get(self, key):
        # Depending on our hash function, if the collision rate is high, then O(n) at worst for retrieving items, else O(1)
        index = self._hash(key)
        return self.table[index].get(key)

    def remove(self, key):
        index = self._hash(key)
        self.table[index].remove(key)

