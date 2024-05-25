# n! = n * (n - 1) * (n - 2) * ... * 2 * 1
# 0! = 1
# n! = n * (n - 1)!

# factorial(n) = n * factorial(n - 1)
# factorial(0) = 1
# factorial(k) = 1, if k <= 1

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    for i in range(11):
        print(f"Factorial of {i} is {factorial(i)}")