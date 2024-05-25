from LinkedList import *

#class LinkStack:
#    def __init__(self):
#        self.__sList = LinkedList()
#
#    def isEmpty(self):
#        return self.__sList.isEmpty()
#    
#    def __len__(self):
#        return len(self.__sList)
#    
#    def __str__(self):
#        return str(self.__sList)
#    
#    def push(self, item):
#        self.__sList.insertFront(item)
#
#    def pop(self):
#        return self.__sList.deleteFirst()
#    
#    def peek(self):
#        return self.__sList.getFirst()

class LinkStack(LinkedList):
    push = LinkedList.insertFront
    pop = LinkedList.deleteFirst
    peek = LinkedList.getFirst