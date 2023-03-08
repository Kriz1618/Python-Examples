def outer_function():
    global a
    a = 20
    
    def inner_func():
        global a
        a = 30
        print('8', 'a', a)
        
    inner_func()
    print('11', 'a', a)
    
a = 10
print('14', 'a', a)
outer_function()
print('16', 'end a', a)