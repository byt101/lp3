# 1. Fibonacci Numbers

# Recursive function
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Non-recursive (loop) method
def fib_non_recursive(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()

n = 10
print("Recursive Fibonacci:")
for i in range(n):
    print(fib_recursive(i), end=" ")
print("\nNon-Recursive Fibonacci:")
fib_non_recursive(n)
