def encode_letter(letter):
    letter = letter.lower()
    if 'a' <= letter and letter <= 'z':
        return ord(letter) - ord('a') + 1  # 'a': 1, 'b': 2, ..., 'z': 26
    return 0

def encode_word(word):
    total = 0
    for i in range(len(word)):
        total += encode_letter(word[i]) * 27 ** (len(word) - 1 - i)
    return total

def simpleHash(key):
    if isinstance(key, int):
        return key
    if isinstance(key, str):
        return encode_word(key)
    raise Exception('Unable to hash key of type ' + str(type(key)))

# start = 5, size = 11
# 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4
def linearProbe(start, size):
    for i in range(size):  # 0, 1, ..., size - 1
        yield (start + i) % size

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):  # 2, 3, 4, ..., n - 1
        if n % i == 0:
            return False
    return True


class HashTable:

    def __init__(self, size=7, hash=simpleHash, probe=linearProbe, maxLoadFactor=0.1):
        self.__table = [None] * size
        self.__nItems = 0
        self.__hashFunction = hash
        self.__probeFunction = probe
        self.__maxLoadFactor = maxLoadFactor

    def __len__(self):
        return self.__nItems

    def cells(self):
        return len(self.__table)  # length of the array

    def hash(self, key):
        return self.__hashFunction(key) % self.cells()

    __Deleted = (None, "Deletion marker") # tuple with 2 items

    def __find(self, key, deletedOK=False):
        for index in self.__probeFunction(self.__hashFunction(key), self.cells()):
            if self.__table[index] is None or (self.__table[index] == HashTable.__Deleted and deletedOK) or self.__table[index][0] == key:
                return index

    def search(self, key):
        index = self.__find(key, deletedOK=False)
        if index is None:
            return None
        if self.__table[index] == None:
            return None
        if self.__table[index][0] != key:
            return None
        return self.__table[index][1]

    def insert(self, key, value):
        index = self.__find(key, deletedOK=True)
        if index is None:
            raise Exception("Hash table probe sequence failed on insert")
        if (self.__table[index] is None or self.__table[index] is HashTable.__Deleted):
            self.__table[index] = (key, value)  # new key value pair is inserted
            self.__nItems += 1
            if self.loadFactor() > self.__maxLoadFactor:
                self.__growTable()
            return True

        if (self.__table[index][0] == key):
            self.__table[index][1] = value
            return False  # only update of the value happened

    def loadFactor(self):
        return self.__nItems / self.cells()

    def __growTable(self):
        oldTable = self.__table
        size = 2 * self.cells() + 1
        while not is_prime(size):
            size += 2
        self.__table = [None] * size
        self.__nItems = 0
        for i in range(len(oldTable)):
            if (oldTable[i] is not None and oldTable[i] is not HashTable.__Deleted):
                self.insert(oldTable[i][0], oldTable[i][1])

    def delete(self, key, ignoreMissing=False):
        index = self.__find(key)
        if index is None or self.__table[index] is None or self.__table[index][0] != key:
            if ignoreMissing:
                return
            raise Exception(f"Cannot delete key {key} not found in hash table")

        self.__table[index] = HashTable.__Deleted
        self.__nItems -= 1

    def traverse(self):
        for i in range(self.cells()):
            if self.__table[i] is not None and self.__table[i] is not HashTable.__Deleted:
                yield self.__table[i]


if __name__ == "__main__":
    dictionary = HashTable()
    dictionary.insert("apple", "alma")
    print(dictionary.search("apple"))
    dictionary.insert("orange", "narancs")
    dictionary.insert("banana", "banán")
    dictionary.insert("chair", "szék")
    dictionary.delete("banana")
    for item in dictionary.traverse():
        print(item)


        