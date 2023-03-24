def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

def ex1():
    class MyClass:
        """A simple example class"""
        i = 12345

        def f(self):
            return 'hello world'
    print('attributes {} {}'.format(MyClass.i, MyClass.f))
    
# ex1()

def ex2():
    class Dog:

        kind = 'canine'     # class variable shared by all instances

        def __init__(self, name):
            self.name = name 

    d = Dog('Fido')
    e = Dog('Buddy')
    print('45', 'd.kind', d.kind)
    print('46', 'e.kind', e.kind)
    print('47', 'd.name', d.name)
    print('48', 'e.name', e.name)
    
# ex2()

def ex3():
    class Dog:
        tricks = []             # mistaken use of a class variable
        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            self.tricks.append(trick)
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    print(d.tricks)
    
# ex3()

def ex3():
    class Dog:
        def __init__(self, name):
            self.name = name
            self.tricks = []    # creates a new empty list for each dog
        
        def add_trick(self, trick):
            self.tricks.append(trick)
    d = Dog('Fido')
    e = Dog('Buddy')
    d.alias = 'Firu'
    d.add_trick('roll over')
    e.add_trick('play dead')
    print(d.tricks, d.alias)
    del d.tricks
    # print('83', 'd', d, d.tricks)
    print(e.tricks)
    
# ex3()

def ex4():
    class Bag:
        def __init__(own):
            own.data = []

        def add(own, x):
            own.data.append(x)

        def addtwice(own, x):
            own.add(x)
            own.add(x)
    my_bag = Bag()
    my_bag.add(3)
    my_bag.addtwice(4)
    print(my_bag.data)

# ex4()

def ex5():
    class Mapping:
        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)

            def update(self, iterable):
                for item in iterable:
                    self.items_list.append(item)

            __update = update   # private copy of original update() method

    class MappingSubclass(Mapping):

        def update(self, keys, values):
            # provides new signature for update()
            # but does not break __init__()
            for item in zip(keys, values):
                self.items_list.append(item)
  
from dataclasses import dataclass
              
def ex5():
    @dataclass
    class Employee:
        name: str
        dept: str
        salary: int
        
    john = Employee('john', 'computer lab', 1000)
    print('136', 'john.dept', john.dept)
    print('137', 'john.salary', john.salary)
# ex5()

def ex6():
    s = 'abc'
    it = iter(s)
    print('143', 'it', it)

    try:
        print('145', 'next(it)', next(it))
        print('146', 'next(it)', next(it))
        print('147', 'next(it)', next(it))
        print('148', 'next(it)', next(it))
    except StopIteration:
        print('Iteration finished!!')
    
# ex6()

def ex7():
    class Reverse:
        """Iterator for looping over a sequence backwards."""
        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]
    rev = Reverse('spam')
    iter(rev)

    for char in rev:
        print(char)
        
# ex7()

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
test = 'golf'  
# print(test, test[::-1])   
# for char in reverse(test):
#     print(char)
    
def ex8():
    print('187', 'sum(i*i for i in range(10)) ', sum(i*i for i in range(10)) )                # sum of squares


    xvec = [10, 20, 30]
    yvec = [7, 5, 3]
    print('192', 'sum(x*y for x,y in zip(xvec, yvec))', sum(x*y for x,y in zip(xvec, yvec)))         # dot product


    # unique_words = set(word for line in page  for word in line.split())
    # valedictorian = max((student.gpa, student.name) for student in graduates)

    data = 'golf'
    list(data[i] for i in range(len(data)-1, -1, -1))
ex8()