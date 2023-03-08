def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print('Factorial of 6 is {}'.format(fact(6)))