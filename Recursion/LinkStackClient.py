from LinkStack import *

myStack = LinkStack()
assert myStack.isEmpty() == True

myStack.push(5)
myStack.push(13)
myStack.push(42)
print(myStack) # __str__() is called

top = myStack.peek()
print(top)

deletedItem = myStack.pop()
print(deletedItem)
