x = 'global'

def funct1():
    global x
    y = 'local'
    x = x * 2
    print('7', 'x', x)
    print('8', 'y', y)
    
# print('Global x = ', x)
# funct1()
# print('Global x = ', x)

a = 5

def func2():
    a = 20
    print('18', 'a', a)
    
# print('20', 'a', a)
# func2()
# print('22', 'a', a)


def outer():
    x = 'local'
    
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('31', 'inner x', x)
        
    inner()
    print('34', 'out x', x)
    
# outer()

def fun1():
    y = 20
    
    def fun2():
        global y
        y = 25
        
    print('Before calling funct 2 ', y)
    fun2()
    print('After calling funct 2 ', y)
    
fun1()
print('Y in main: ', y)