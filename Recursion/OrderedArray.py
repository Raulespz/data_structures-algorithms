class OrderedArray(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems
    
    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]
        raise IndexError("Index " + str(n) + " is out of range")
    
    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans += "]"
        return ans
    
    # def find(self, item): # iterative
    #     lo = 0
    #     hi = self.__nItems - 1

    #     while lo <= hi:
    #         mid = (lo + hi) // 2
    #         if self.__a[mid] == item:
    #             return mid
    #         elif self.__a[mid] < item:
    #             lo = mid + 1
    #         else:
    #             hi = mid - 1
    #     return lo   # Item not found, return insertion point instead

    def find(self, item, lo=0, hi=None): # recursive
        if hi == None:
            hi = self.__nItems - 1
        if lo > hi: # base case
            return lo # Item not found, return insertion point instead
        mid = (lo + hi) // 2
        if self.__a[mid] == item:
            return mid
        if item < self.__a[mid]:
            return self.find(item, lo, mid - 1) # hi = mid - 1
        return self.find(item, mid + 1, hi) # lo = mid + 1
    
    def search(self, item):
        index = self.find(item)
        if index < self.__nItems and self.__a[index] == item:
            return self.__a[index]
        
    def insert(self, item):
        if self.__nItems >= len(self.__a):
            raise Exception("Array overflow")
        index = self.find(item)
        for j in range(self.__nItems, index, -1):
            self.__a[j] = self.__a[j - 1]
        self.__a[index] = item
        self.__nItems += 1

    def delete(self, item):
        j = self.find(item)
        if j < self.__nItems and self.__a[j] == item:
            self.__nItems -= 1
            for k in range(j, self.__nItems):
                self.__a[k] = self.__a[k + 1]
            return True
        return False
    
if __name__ == "__main__":
    arr = OrderedArray(10)
    arr.insert(3)
    arr.insert(8)
    arr.insert(11)
    arr.insert(42)
    arr.insert(54)
    arr.insert(60)

    print(arr.find(11))
    print(arr.search(12))
    print(arr.search(11))
    arr.delete(11)
    print(arr)