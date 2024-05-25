import SortArray
import random

class Array(SortArray.Array):

    def shellSort(self):

        # Calculate the initial distance of postitions (h)
        h = 1
        while 3 * h + 1 < len(self):
            h = 3 * h + 1

        nShifts = 0
        # Algorithm of shell sort
        while h > 0:
            for outer in range(h, len(self)):
                temp = self.get(outer)
                inner = outer
                while inner >= h and temp < self.get(inner - h):
                    self.set(inner, self.get(inner - h))
                    nShifts += 1
                    inner -= h

                self.set(inner, temp)

            h = (h - 1) // 3

        return nShifts
    
    def copy(self):
        arr = Array(len(self))
        for i in range(len(self)):
            arr.insert(self.get(i))
        return arr


def initArray(size=100, maxValue=100, seed=2.14159):
    arr = Array(size)
    random.seed(seed)
    for i in range(size):
        arr.insert(random.randrange(maxValue))
    return arr



if __name__ == "__main__": # runs if this modul is run from the terminal
    arr = initArray(size=10000, maxValue=1000000)
    # print(arr)

    arr1 = arr.copy()
    # print(arr1)

    nShifts = arr1.insertionSort()
    print("Sorted using insertion sort")
    # print(arr1)
    print(f"Number of shifts: {nShifts}")

    
    nShifts = arr.shellSort()
    print("Sorted using shell sort")
    # print(arr) # sorted array
    print(f"Number of shifts: {nShifts}")

