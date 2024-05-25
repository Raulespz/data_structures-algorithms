from SimpleStack import *

stack = Stack(100)

word = input("Word to reverse: ")

for letter in word:
    if not stack.isFull():
        stack.push(letter)

reverse = ''
while not stack.isEmpty():
    reverse += stack.pop()

print(f"The reverse of {word} is {reverse}")
