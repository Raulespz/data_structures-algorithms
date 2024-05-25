class Linkedlist:

    class Node:
        def __init__(self, data, next=None):
            self.__data = data
            self.__next = next

        def getData(self):
            return self.__data
        
        def setData(self, newData):
            self.__data = newData

        def getNext(self):
            return self.__next
        
        def setNext(self, newLink):
            if newLink is None or isinstance(newLink, Linkedlist.Node):
                self.__next = newLink
            else:
                raise Exception("Next mode must to be a Node")
            
        def isLast(self) -> bool:
            return self.__next == None
        
        def __str__(self):
            return str(self.__data) 
        
    def __init__(self):
        self.__head = None
    
    def isEmpty(self) -> bool:
        return self.__head == None
    
    def insertFront(self, newData):
        newNode = Linkedlist.Node(data=newData, next=self.__head)
        self.__head = newNode

    def traverse(self, func=print):
        currentNode = self.__head
        while currentNode is not None:
            func(currentNode.getData())
            currentNode = currentNode.getNext()

    def __len__(self):
        count = 0
        currentNode = self.__head
        while currentNode is not None:
            count += 1
            currentNode = currentNode.getNext()
        return count
    
    def __str__(self):
        result = "["
        currentNode = self.__head
        while currentNode is not None:
            if len(result) > 1:
                result += " > "
            result += str(currentNode)
            currentNode = currentNode.getNext()
        result += "]"
        return result
    



