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
    
    def find(self, item):
        lo = 0
        hi = self.__nItems - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if self.__a[mid] == item:
                return mid
            elif self.__a[mid] < item:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo   # Item not found, return insertion point instead
    
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
    