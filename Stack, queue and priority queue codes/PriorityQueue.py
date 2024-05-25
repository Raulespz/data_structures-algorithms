def identity(x):
    return x

class PriorityQueue(object):
    def __init__(self, size, priority=identity):
        self.__maxSize = size
        self.__queue = [None] * size
        self.__priority = priority
        self.__nItems = 0

    def insert(self, item):
        if self.isFull():
            raise Exception("Queue overflow")
        j = self.__nItems - 1
        while j >= 0 and self.__priority(item) >= self.__priority(self.__queue[j]):
            self.__queue[j + 1] = self.__queue[j]
            j -= 1
        self.__queue[j + 1] = item
        self.__nItems += 1
        return True
    
    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        self.__nItems -= 1
        front = self.__queue[self.__nItems]
        self.__queue[self.__nItems] = None
        return front
    
    def peek(self):
        return None if self.isEmpty() else self.__queue[self.__nItems - 1]
    
    def isEmpty(self):
        return self.__nItems == 0
    
    def isFull(self):
        return self.__nItems == self.__maxSize
    
    def __len__(self):
        return self.__nItems
    
    def __str__(self):
        ans = "["
        for i in range(self.__nItems - 1, -1, -1):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__queue[i])
        ans += "]"
        return ans
