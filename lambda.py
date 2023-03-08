a = lambda x: x*2

for i in range(1,6):
    print(a(i))
    
    
def outer_func():
    a = 5
    def inner_func():
        nonlocal a
        a = 10
        print('Inner func: ', a)
    inner_func()
    print('Outer func: ', a)
    
outer_func()