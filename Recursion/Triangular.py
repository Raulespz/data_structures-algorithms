def triangular_loop(nth): # Generates the n-th triangular number
    total = 0
    for i in range(1, nth + 1): # 1, 2, 3, 4, ..., n
        total += i # total = total + i
    return total

def triangular(nth): # Do not use any loops
    if nth == 1:
        return 1
    return nth + triangular(nth - 1)

def show_triangular(nth):
    print(f"Computing triangular number #{nth}")
    if nth == 1:
        print("Base case. Returning 1.")
        return 1
    value = nth + show_triangular(nth - 1)
    print(f"Returning {value} for #{nth}")
    return value

if __name__ == "__main__":
#    for n in range(1, 11):
#        print(f"{n}-th triangular number is: {triangular(n)}")
    show_triangular(5)