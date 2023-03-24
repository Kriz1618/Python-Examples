def func(x):
    return x * 3


new_func = func


def func(x):
    return x + 5


# print(new_func(4))
# print(func(4))


def hello(name, msg = ', how are you?'):
    print('Hello', name, msg)
    
# hello('Ansu', ', Good evening!!')
# hello('Ansu')

def sumAll(*args):
    sum = 0
    for i  in args:
        sum += i if str(i).isnumeric() else 0
    return sum

# print(sumAll(1,2,3,4,6,'y',5))

def defaultArg(a, b, c):
    print("a = {}, b = {}, c = {}...".format(a,b,c))
    
# defaultArg(5, 8, 9)

import random as r

def guess_num():
    rand_num = r.randrange(1, 15)
    print('Number to be guesses: ', rand_num)
    
    i = 1
    
    while True:
        print('Number guessed: ', i)
        if i == rand_num:
            print('Random Number was guessed!!')
            break
        i += 1
    print('End')
    
# guess_num()

# for i in range(1, 20):
#     print(i)
#     if i%2 != 0:
#         continue
#     print('Even', i)
    
    
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5

def f(arg=i):
    print(arg)

i = 6
# f()

def f(a, L=[]):
    L.append(a)
    return L

# print(f(1))
# print(f(2))
# print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# print(f(5,[2, 6]))
# print(f(5))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!\n")
    
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?\n")
    print("-- I'm sorry, we're all out of", kind, '\n')
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
# cheeseshop("Limburger", "It's very runny, sir.",
#         "It's really very, VERY runny, sir.",
#         shopkeeper="Michael Palin",
#         client="John Cleese",
#         sketch="Cheese Shop Sketch")

def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
    
# standard_arg(2)
# standard_arg(arg=2)

# pos_only_arg(1)
# pos_only_arg(arg=1) # will raice an error

# kwd_only_arg(3) # will raice an error
# kwd_only_arg(arg=3)

combined_example(1, 2, 3) # will raice an error
combined_example(1, 2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # will raice an error

def foo(name, **kwds):
    return 'name' in kwds

# foo(1, **{'name': 2}) # will raice an error

def foo(name, /, **kwds):
    print('156', 'name', name)
    return 'name' in kwds

# print(foo(1, **{'name': 2}))

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
    
def concat(*args, sep="/"):
    res = sep.join(args)
    print('165', 'res', res)

# concat("earth", "mars", "venus")
# concat("earth", "mars", "venus", sep=".")

# print(list(range(3, 6)))
# args = [3, 11, 2]
# print(list(range(*args)))

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
    
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

def make_incrementor(n):
   return lambda x: x + n

# f = make_incrementor(42)
# print(f(0))
# print(f(1))

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print('191', 'pairs', pairs)

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

# print(my_function.__doc__)

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

# f('spam')

def total_fruits(**kwargs):
    print(kwargs, type(kwargs))


# total_fruits(banana=5, mango=7, apple=8)

def total_fruits(**fruits):
    print('216', 'fruits', fruits)
    total = 0
    for amount in fruits.values():
        total += amount
    return total


# print(total_fruits(banana=5, mango=7, apple=8))
# print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
# print(total_fruits(banana=5, mango=7),'\n')

def add(*numbers):
    print('227', 'numbers', numbers)
    total = 0
    for num in numbers:
        total += num
    return total


# print(add(2, 3))
# print(add(2, 3, 5))
# print(add(2, 3, 5, 7))
# print(add(2, 3, 5, 7, 9))

def hi():
    return "hi yasoob!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

# doSomethingBeforeHi(hi)