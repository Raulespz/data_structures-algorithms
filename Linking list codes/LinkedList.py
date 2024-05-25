def identity(x):
    return x

class LinkedList:

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
            if newLink is None or isinstance(newLink, LinkedList.Node): # newlink's type is LinkedList.Node
                self.__next = newLink
            else:
                raise Exception("Next node must be a Node")

        def isLast(self) -> bool:
            return self.__next == None
        
        def __str__(self):
            return str(self.__data)
        
    def __init__(self):
        self.__head = None

    def isEmpty(self) -> bool:
        return self.__head == None
    
    def insertFront(self, newData):
        newNode = LinkedList.Node(data=newData, next=self.__head)
        self.__head = newNode

    def insertBack(self, newData):
        if self.isEmpty():
            self.insertFront(newData)
            return
        
        currentNode = self.__head
        while currentNode.getNext() is not None:
            currentNode = currentNode.getNext()
        newNode = LinkedList.Node(data=newData)
        currentNode.setNext(newNode)

    def find(self, keygoal, key=identity):
        currentNode = self.__head
        while currentNode is not None:
            if keygoal == key(currentNode.getData()):
                return currentNode
            currentNode = currentNode.getNext()
        return None
    
    def search(self, keygoal, key=identity):
        foundNode = self.find(keygoal, key)
        if foundNode is not None:
            return foundNode.getData()
        return None
    
    def insertAfter(self, goal, newData, key=identity):
        foundNode = self.find(goal, key)
        if foundNode is None:
            self.insertBack(newData)
        else:
            newNode = LinkedList.Node(data=newData, next=foundNode.getNext())
            foundNode.setNext(newNode)

    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("Cannot delete first item from an empty list")
        
        result = self.__head.getData()
        self.__head = self.__head.getNext()
        return result
    
    def delete(self, goalKey, key=identity):
        if self.isEmpty():
            raise Exception("Cannot delete first item from an empty list")
        
        if goalKey == key(self.__head.getData()):
            return self.deleteFirst()
        
        previousNode = self.__head
        while previousNode.getNext() is not None and key(previousNode.getNext().getData()) != goalKey:
            previousNode = previousNode.getNext()
        
        if previousNode.getNext() is None:
            raise Exception("No item with matching key found in list")
        
        result = previousNode.getNext().getData()
        previousNode.setNext(previousNode.getNext().getNext())
        return result

    def traverse(self, func=print):
        currentNode = self.__head
        while currentNode is not None:
            func(currentNode.getData())
            currentNode = currentNode.getNext() # update currentNode

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