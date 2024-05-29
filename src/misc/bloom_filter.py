
from typing import Optional


def adler32(data: str) -> int:
    MOD_ADLER = 65521
    a = 1
    b = 0
    for char in data:
        a = (a + ord(char)) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a

def djb2(data: str) -> int:
    hash = 5381
    for char in data:
        hash = ((hash << 5) + hash) + ord(char)  # hash * 33 + c
    return hash

def fnv1a(data: str) -> int:
    hash = 2166136261
    for char in data:
        hash ^= ord(char)
        hash *= 16777619
    return hash

def sdbm(data: str) -> int:
    hash = 0
    for char in data:
        hash = ord(char) + (hash << 6) + (hash << 16) - hash
    return hash

class BloomFilter:
    #### Experimental - Bloom filter
    # https://en.wikipedia.org/wiki/Bloom_filter
    # It's a test to see if the key is definitely not in the set or maybe in the set
    # Let's select 4 hash functions --- k = 4
    # m is variable, the size of the bit array
    def __init__(self, size: Optional[int] = 24):
        self.size = size
        self.bit_array = [0] * size

    def add(self, key: str):
        self.bit_array[self._hash1(key) % self.size] = 1
        self.bit_array[self._hash2(key) % self.size] = 1
        self.bit_array[self._hash3(key) % self.size] = 1
        self.bit_array[self._hash4(key) % self.size] = 1

    def contains(self, key: str) -> bool:
        return self.bit_array[self._hash1(key) % self.size] == 1 and self.bit_array[self._hash2(key) % self.size] == 1 and self.bit_array[self._hash3(key) % self.size] == 1 and self.bit_array[self._hash4(key) % self.size] == 1

    def _hash1(self, key: str) -> int:
        return adler32(key)

    def _hash2(self, key: str) -> int:
        return djb2(key)

    def _hash3(self, key: str) -> int:
        return fnv1a(key)
    
    def _hash4(self, key: str) -> int:
        return sdbm(key)