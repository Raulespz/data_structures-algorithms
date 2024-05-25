from LinkedList import *

link = LinkedList.Node(data=2)
assert link.isLast() == True
assert link.getData() == 2
assert link.getNext() == None

link2 = LinkedList.Node(3, link)
assert link2.isLast() == False
assert link2.getData() == 3
link2.setData(5)
assert link2.getData() == 5
assert link2.getNext() == link

link3 = LinkedList.Node(5)
link3.setNext(link2)
assert link3.getNext() == link2

isAssertionRaised = False
try:
    link3.setNext(8)
except Exception:
    isAssertionRaised = True
assert isAssertionRaised == True

link3.setNext(None)
assert link3.isLast() == True

linkedList1 = LinkedList()
assert linkedList1.isEmpty() == True
linkedList1.insertFront(32)
assert linkedList1.isEmpty() == False
linkedList1.insertFront(43)
# linkedList1.traverse()
assert len(linkedList1) == 2
assert str(linkedList1) == "[43 > 32]"

linkedList1.insertBack(56)
assert len(linkedList1) == 3
assert str(linkedList1) == "[43 > 32 > 56]"
foundNode = linkedList1.find(32)
assert foundNode is not None
assert linkedList1.search(32) == 32
foundNode = linkedList1.find(12)
assert foundNode is None
linkedList1.insertAfter(32, 17)
assert len(linkedList1) == 4
assert str(linkedList1) == "[43 > 32 > 17 > 56]"
assert linkedList1.deleteFirst() == 43
assert len(linkedList1) == 3
assert str(linkedList1) == "[32 > 17 > 56]"
linkedList1.delete(17)
assert len(linkedList1) == 2
assert str(linkedList1) == "[32 > 56]"
linkedList1.delete(56)
assert len(linkedList1) == 1
assert str(linkedList1) == "[32]"

def square(x):
    return x * x

foundNode = linkedList1.find(1024, square)
assert foundNode is not None
assert linkedList1.search(1024, square) == 32

linkedList1.delete(32)
assert len(linkedList1) == 0
assert str(linkedList1) == "[]"


linkdedList2 = LinkedList()
assert linkdedList2.isEmpty() == True
isAssertionRaised = False
try:
    linkdedList2.deleteFirst()
except Exception as ex:
    assert str(ex) == "Cannot delete first item from an empty list"
    isAssertionRaised = True
assert isAssertionRaised == True

linkdedList2.insertBack(78)
assert len(linkdedList2) == 1
assert str(linkdedList2) == "[78]"