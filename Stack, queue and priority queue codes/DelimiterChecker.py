from SimpleStack import *

stack = Stack(100)

expr = input("Expression to check: ")

errors = 0

for pos, letter in enumerate(expr):
    if letter in "{[(":
        if stack.isFull():
            raise Exception('Stack overflow on expression')
        else:
            stack.push(letter)
    elif letter in "}])":
        if stack.isEmpty():
            print(f"Error: {letter} at position {pos} ha no matching left delimiter")
            errors += 1
        else:
            left = stack.pop()
            if not (left == "{" and letter == "}" or
                    left == "[" and letter == "]" or
                    left == "(" and letter == ")"):
                print(f"Error: {letter} at position {pos} does not match left delimiter {left}")
                errors += 1

if stack.isEmpty() and errors == 0:
    print(f"Delimiters balance in expression {expr}")
elif not stack.isEmpty():
    print(f"Expression missing right delimiters for {stack}")
