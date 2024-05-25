from linkedlist import *

link = Linkedlist.Node(data=2)
assert link.isLast() == True
assert link.getData() ==2
assert link.getNext() == None

link2 = Linkedlist.Node(3, link)
assert link2.isLast() == False
assert link2.getData() ==3
link2.setData(5)
assert link2.getData() == 5
assert link2.getNext() == link

link3 = Linkedlist.Node(5)
link3.setNext(link2)
assert link3.getNext() == link2

isAsertionraise = False
try: 
    link3.setNext(8)
except Exception:
    isAsertionraise = True
assert isAsertionraise == True

link3.setNext(None)
assert link3.isLast() == True

Linkedlist1 = Linkedlist()
assert Linkedlist1.isEmpty() == True
Linkedlist1.insertFront(32)
assert Linkedlist1.isEmpty() == False
Linkedlist1.insertFront(43)
#Linkedlist1.traverse()
assert len(Linkedlist1) == 2

print(Linkedlist1)

