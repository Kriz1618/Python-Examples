# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print(fib(5))
def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

def fibonacci(n):
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-2]+fib[i-1])
    return fib[:n]

# [fibonacci_of(n) for n in range(15)]
fibonacci(8)

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2:
        fib(int(sys.argv[1]))
# Now enter the Python interpreter and import this module with the following command: import fibo



