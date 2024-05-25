import SortArray
import random

class Array(SortArray.Array):

    def partition_rec(self, pivot, lo=0, hi=None):
        if hi is None:
            hi = len(self) - 1 # index to the last item

        # finds the first item which is greater than pivot
        while lo <= hi and self.get(lo) <= pivot:
            lo += 1

        # finds the last item which is not greater than pivot
        while lo < hi and pivot < self.get(hi):
            hi -= 1

        if lo >= hi:
            return lo
        
        self.swap(lo, hi)

        return self.partition_rec(pivot, lo + 1, hi - 1)
    
    def partition(self, pivot, lo=0, hi=None):
        if hi is None:
            hi = len(self) - 1

        while lo <= hi:
            # finds the first item which is greater than pivot
            while lo <= hi and self.get(lo) <= pivot:
                lo += 1

            # finds the last item which is not greater than pivot
            while lo < hi and pivot < self.get(hi):
                hi -= 1

            if lo >= hi:
                return lo
            
            self.swap(lo, hi)
            lo += 1
            hi -= 1

        return lo

    def quicksort(self, lo=0, hi=None):
        if hi is None:
            hi = len(self) - 1

        if lo >= hi:
            return
        
        pivotIdxBeforePartition = hi
        pivotItem = self.get(pivotIdxBeforePartition)

        pivotIdxAfterPartition = self.partition(pivotItem, lo, hi - 1)

        if pivotIdxAfterPartition < pivotIdxBeforePartition:
            self.swap(pivotIdxBeforePartition, pivotIdxAfterPartition)
        
        self.quicksort(lo, pivotIdxAfterPartition - 1)
        self.quicksort(pivotIdxAfterPartition + 1, hi)
    

def initArray(size=100, maxValue=100, seed=2.14159):
    arr = Array(size)
    random.seed(seed)
    for i in range(size):
        arr.insert(random.randrange(maxValue))
    return arr


if __name__ == "__main__":
    arr = initArray(30)
    print(arr)

    arr.quicksort()
    print(arr)

    # idx = arr.partition(50)
    # print(arr)
    # print(f"Index: {idx}")