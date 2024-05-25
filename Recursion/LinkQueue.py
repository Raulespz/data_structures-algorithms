from LinkedList import *

class LinkQueue(LinkedList):
    enqueue = LinkedList.insertBack
    dequeue = LinkedList.deleteFirst
    peek = LinkedList.getFirst
