def identity(x):
    return x

class Heap:

    def __init__(self, key=identity, size=2):
        self._array = [None] * size
        self._nItems = 0
        self._key = key

    def isEmpty(self):
        return self._nItems == 0

    def isFull(self):
        return self._nItems == len(self._array)

    def __len__(self):
        return self._nItems

    def peek(self):
        return None if self.isEmpty() else self._arr[0]

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def insert(self, item): # O(log(n))
        if self.isFull():
            self._growHeap()

        self._array[self._nItems] = item  # O(1)
        self._nItems += 1
        
        self._siftUp(self._nItems - 1) # O(log(n))

    def _growHeap(self):
        currentArray = self._array
        self._array = [None] * max(1, 2 * len(currentArray))
        for i in range(self._nItems):
            self._array[i] = currentArray[i]

    def _siftUp(self, i):  # O(log(n))
        if i <= 0: # i is the index of root or a non valid index
            return
        
        item = self._array[i]
        itemkey = self._key(item)
        while 0 < i:
            parentIdx = self.parent(i)
            if self._key(self._array[parentIdx]) < itemkey:
                self._array[i] = self._array[parentIdx]
                i = parentIdx
            else:
                break
        self._array[i] = item

    def remove(self):  # Removes the top item, O(log(n))
        if self.isEmpty():
            raise Exception("Heap underflow")

        root = self._array[0]

        self._nItems -= 1
        self._array[0] = self._array[self._nItems]
        self._array[self._nItems] = None
        self._siftDown(0)

        return root

    def _siftDown(self, i): # O(log(n))
        if i >= self._nItems:  # i is an invalid index
            return

        item = self._array[i]
        itemkey = self._key(item)
        while i < self._nItems:  # while i is a valid index
            leftIndex = self.leftChild(i)
            rightIndex = self.rightChild(i)

            maxIndex = leftIndex
            if (rightIndex < self._nItems and self._key(self._array[leftIndex]) < self._key(self._array[rightIndex])):
                maxIndex = rightIndex
            if maxIndex < self._nItems and itemkey < self._key(self._array[maxIndex]):
                self._array[i] = self._array[maxIndex]
                i = maxIndex
            else:
                break
        self._array[i] = item

    def traverse(self):
        for i in range(self._nItems):
            yield self._array[i]


def heapsort(array):
    heap = Heap()
    for item in array: # O(n log(n))
        heap.insert(item) # O(log(n))
    result = []
    while not heap.isEmpty(): # O(n log(n))
        result.insert(0, heap.remove()) # O(log(n))
    return result

if __name__ == "__main__":

    array = [34, 56, 1, 23, 42, 89, 43, 28]
    for item in heapsort(array):
        print(item)
    
    # heap = Heap()

    # heap.insert(43)
    # heap.insert(24)
    # heap.insert(56)
    # heap.insert(78)
    # heap.insert(42)
    # heap.insert(28)

    # for item in heap.traverse():
    #     print(item)

    # while not heap.isEmpty():
    #     print(heap.remove())