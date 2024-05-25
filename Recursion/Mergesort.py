from Array import *

class Mergesort:
    def __init__(self, unordered):
        self.__array = unordered
        n = len(unordered)
        self.__workingArray = Array(n)
        for i in range(n):
            self.__workingArray.insert(None)
        self.mergesort(0, n)
    
    def mergesort(self, lo, hi): # lo and hi are indices
        if lo + 1 >= hi: # subarray has max 1 element => the subarray is sorted
            return
        
        mid = (lo + hi) // 2
        self.mergesort(lo, mid) # sorting of the left subarray
        self.mergesort(mid, hi) # sorting of the right subarray
        self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):
        idxLo = lo # index in the left subarray, initialized to the start
        idxHi = mid # index in the right subarray, initialized to the start
        n = 0

        while idxLo < mid and idxHi < hi:
            itemLo = self.__array.get(idxLo)
            itemHi = self.__array.get(idxHi)
            if itemLo <= itemHi:
                self.__workingArray.set(n, itemLo) # insert from the left subarray
                idxLo += 1
            else:
                self.__workingArray.set(n, itemHi) # insert from the right subarray
                idxHi += 1
            n += 1
        while idxLo < mid:
            itemLo = self.__array.get(idxLo)
            self.__workingArray.set(n, itemLo)
            idxLo += 1
            n += 1
        while n > 0:
            n -= 1
            self.__array.set(lo + n, self.__workingArray.get(n))

if __name__ == "__main__":
    values = [19, 49, 70, 72, 43, 80, 95, 46, 19, 18, 45, 6, 56, 85]
    array = Array(len(values))

    for value in values:
        array.insert(value)

    print(f"Initial array contains {len(array)} items")
    array.traverse()

    Mergesort(array)

    print(f"After applying Mergesort, array contains {len(array)} items")
    array.traverse()