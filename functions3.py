from functools import cache, cached_property, cmp_to_key, lru_cache, wraps
import time

def exm1():
    @cache
    def factorial(n):
        return n * factorial(n-1) if n else 1

    init = time.process_time()
    print(factorial(10))    # no previously cached result, makes 11 recursive calls
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

from timeit import default_timer as timer

def login_time_decorator(func):
    @wraps(func)    
    def wra_function(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print('Function {} executed on {} secs\n'.format(func.__name__, end - start))
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

import urllib.request as req
import urllib.error as err

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


import sys

def print_argv():
    # python functions3.py 5, 6, False
    print(sys.argv)
    
# print_argv()

from functools import total_ordering

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