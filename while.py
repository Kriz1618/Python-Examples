i = 3
while i > 0:
    print(i)
    i -= 1
    
while i < 10:
    print(i)
    i += 1
# else:
print('finish loop')    


def print_layers():
    n = int(input('Type the number of layers: '))
    i = 1
    
    while i <= n:
        j = 1
        while j <= n-i:
            print(".",end="")
            j = j + 1
        j = 1
        while j <= 2*i - 1:
            print("*",end="")
            j += 1
        print()
        i += 1

# print_layers()          

def print_layers2():
    n, i = int(input('Type the number of layers: ')), 1
    
    while i <= n:
        print('.' * (n - i), '*' * (2*i -1))
        i += 1
# print_layers2()

def print_layers():
    n = int(input('Type the odd number of layers: '))
    i = 1
    m = (n+1)/2
    
    while i <= n:
        if i > m:
            b = n - i
            s = 2 * (i-m) + 1
        else:
            b = i-1
            s = 2 * (m-i) + 1
        j = 1
        while j <= b:
            print(".",end="")
            j = j + 1
        j = 1
        while j <= s:
            print("*",end="")
            j += 1
        print()
        i += 1
        
# print_layers()

def fibonacci_series(num):
    a, b = 0, 1
    while a < num:
       print(a)
       a, b = b, a+b
       
fibonacci_series(10)
        