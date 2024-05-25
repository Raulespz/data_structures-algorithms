class Array(object):

    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0
    
    def get_size(self):
        return self.__nItems
    
    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def search(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return self.__a[j]
        return None
    
    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k + 1]
                self.__nItems -= 1
                return True
        return False
    
    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])
