from decimal import Decimal
from functools import singledispatch
import operator
from functools import total_ordering
import urllib.request as req
from timeit import default_timer as timer
from functools import partial, partialmethod
import sys
import urllib.error as err
from functools import cache, cached_property, cmp_to_key, lru_cache, wraps, reduce
import time


def exm1():
    @cache
    def factorial(n):
        return n * factorial(n-1) if n else 1

    init = time.process_time()
    # no previously cached result, makes 11 recursive calls
    print(factorial(10))
    t1 = time.process_time()
    print('Time 1: ',  (init - t1)/1000)

    init2 = time.process_time()
    print(factorial(5))       # just looks up cached value result
    t2 = time.process_time()
    print('Time 2: ',  (init2 - t2)/1000)

    init3 = time.process_time()
    print(factorial(12))
    t3 = time.process_time()
    print('Time 3: ',  (init3 - t3)/1000)

# exm1()


def cached_property_exm():
    class MyClass:
        def __init__(self, some_data):
            self._some_data = some_data

        @cached_property
        def expensive_property(self):
            print("Computing expensive property...")
            # Some expensive computation goes here
            result = self._some_data * 2
            return result

    # Create an instance of MyClass
    obj = MyClass(10)
    print('With cached_property decorator {}'.format(obj.expensive_property))

    class SameClass:
        def __init__(self, some_data):
            self._some_data = some_data

        @property
        @cache
        def expensive_property(self):
            print("Computing expensive property...")
            # Some expensive computation goes here
            result = self._some_data * 2
            return result
    obj = SameClass(10)
    print('With property and cache decorators {}'.format(obj.expensive_property))
# cached_property_exm()


def login_time_decorator(func):
    @wraps(func)
    def wra_function(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print('Function {} executed in {} secs\n'.format(
            func.__name__, end - start))
    return wra_function


def cmp_to_key_exm():
    lst = [(1, 5), (2, 3), (3, 10), (4, 8)]

    def compare_tuples(t1, t2):
        return t2[1] - t1[1]

    @login_time_decorator
    def sort1(lst):
        sorted_lst = sorted(lst, key=cmp_to_key(compare_tuples))
        print('Sorted by using cmp_to_key {}\n'.format(sorted_lst))

    @login_time_decorator
    def sort2(lst):
        second_list = sorted(lst, key=lambda val: val[1], reverse=True)
        print('Sorted with lambda function {}\n'.format(second_list))

    sort1(lst)
    sort2(lst)

# cmp_to_key_exm()


def lru_cache_exm():
    @lru_cache(maxsize=None)
    def fibonacci(n):
        print('*' * n)
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    print(fibonacci(10))
    print(fibonacci(10))
    print(fibonacci(5))
    print(fibonacci(10))
    print(fibonacci(5))

# lru_cache_exm()


def lru_cache_exm1():
    @lru_cache(maxsize=32)
    def get_pep(num):
        'Retrieve text of a Python Enhancement Proposal'
        resource = 'https://peps.python.org/pep-%04d/' % num
        try:
            with req.urlopen(resource) as s:
                return s.read()
        except err.HTTPError:
            return 'Not Found'
    for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
        pep = get_pep(n)
        print(n, len(pep))
    print(get_pep.cache_info())

# lru_cache_exm1()


def print_argv():
    # python functions3.py 5, 6, False
    print(sys.argv)

# print_argv()


def total_ordering_exm():
    @total_ordering
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __eq__(self, other):
            return self.age == other.age

        def __lt__(self, other):
            return self.age < other.age

    p1 = Person("Alice", 25)
    p2 = Person("Bob", 30)
    p3 = Person("Charlie", 25)

    print(p1 < p2)
    print(p1 <= p3)
    print(p1 > p3)
    print(p2 >= p3)
    print('ali'.__eq__('alis'))


# total_ordering_exm()


def partial_exm():
    def add(x, y):
        return x + y

    def multiply(x, y):
        return x * y

    add_five = partial(add, 5)
    double = partial(multiply, y=2)
    basetwo = partial(int, base=2)

    print(add_five(3))
    print(double(5))
    print(basetwo('10010'))
# partial_exm()


def partialmethod_emx():
    class Cell:
        def __init__(self):
            self._alive = False

        @property
        def alive(self):
            return self._alive

        def set_state(self, state):
            self._alive = bool(state)
        set_alive = partialmethod(set_state, True)
        set_dead = partialmethod(set_state, False)
    c = Cell()
    print(c.alive)

    c.set_alive()
    print(c.alive)


# partialmethod_emx()


def reduce_exm():
    arr = [1, 2, 3, 4, 5, 6]
    result = reduce(lambda x, y: x + y, arr)
    print(result)

    result1 = reduce(operator.add, arr)
    print(result1)


# reduce_exm()


def singledispatch_exm():
    @singledispatch
    def fun(arg, verbose=False):
        if verbose:
            print("Let me just say,", end=" ")
        print(arg)

    @fun.register
    def _(arg: int, verbose=False):
        if verbose:
            print("Strength in numbers, eh?", end=" ")
        print(arg)

    @fun.register
    def _(arg: list, verbose=False):
        if verbose:
            print("Enumerate this:")
        for i, elem in enumerate(arg):
            print(i, elem)
            
    @fun.register
    def _(arg: int | float, verbose=False):
        if verbose:
            print("Strength in numbers, eh?", end=" ")
        print(arg)

    from typing import Union
    @fun.register
    def _(arg: Union[list, set], verbose=False):
        if verbose:
            print("Enumerate this:")
        for i, elem in enumerate(arg):
            print(i, elem)
            
    @fun.register(complex)
    def _(arg, verbose=False):
        if verbose:
            print("Better than complicated.", end=" ")
        print(arg.real, arg.imag)
        
    def nothing(arg, verbose=False):
        print("Nothing.")

    fun.register(type(None), nothing)
    
    @fun.register(float)
    @fun.register(Decimal)
    def fun_num(arg, verbose=False):
        if verbose:
            print("Half of your number:", end=" ")
        print(arg / 2)

    fun_num is fun
    
    print(fun("Hello, world."))
    print(fun("test.", verbose=True))
    print(fun(42, verbose=True))
    print(fun(['spam', 'spam', 'eggs', 'spam'], verbose=True))
    fun(None)
    fun(1.23)
    
# singledispatch_exm()

def update_wrapper_exm():
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Before the function is called.")
            result = func(*args, **kwargs)
            print("After the function is called.")
            return result
        return wrapper

    @my_decorator
    def my_function():
        """This is the docstring of my_function."""
        pass

    print(my_function.__name__)  # Output: my_function
    print(my_function.__doc__)
    
# update_wrapper_exm()

def verify_positive_and_palindrome(arr):
    print(all(x > 0 for x in arr) and any(str(x) == str(x)[::-1] for x in arr))

arr = [32, 14, 50, 61]
# verify_positive_and_palindrome(arr)

def custom_sort(w):
    arr = list(w)
    l, u, o, e = [], [], [], []
    print(arr)
    for chart in arr:
        if str.islower(chart):
            l.append(chart)
        elif str.isupper(chart):
            u.append(chart)
        elif str.isnumeric(chart)  and int(chart) % 2 != 0:
            o.append(chart)
        elif str.isnumeric(chart)  and int(chart) % 2 == 0:
            e.append(chart)
    print(l, u, o, e)
    print(''.join(sorted(l) + sorted(u) + sorted(o) + sorted(e)))
    
custom_sort('Sorting1234')