import inspect

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def introspect_object():
    p = Person("John", 25)

    print(type(p), '\n')
    print(type(''), '\n')
    print(type([]), '\n')
    print(dir(p), '\n')
    print(vars(p), '\n')
    print(inspect.getmembers(p), '\n')
    
# introspect_object()

def special_attr():
    p = Person("Xamier", 325)
    
    print(f'dict {p.__dict__}')
    print(f'class {p.__class__}')
    print(f'bases {Person.__bases__}')
    print(f'name {p.__ne__}')
    print(f'mro {Person.__mro__}')
    
# special_attr()

def magic_methods():
    class GetTest(object):
        def __init__(self):
            self.info = {
                'name':'Yasoob',
                'country':'Pakistan',
                'number':12345812
            }

        def __getitem__(self,i):
            return self.info[i]

    foo = GetTest()
    print(foo['name'], foo['number'])
    
magic_methods()

class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __eq__(self, other):
        return self.value == other.value