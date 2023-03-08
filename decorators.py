def make_decorated(func):
    def inner_function():
        print('Decorated!!')
        func()
    return inner_function

def simple_func():
    print('Simple function')

@make_decorated
def other_func():
    print('Second simple function')
    
decor = make_decorated(simple_func)
# decor()
# other_func()

def smart_div(func):
    def inner_func(x, y):
        print('Dividing ', x, 'by ', y)
        if y == 0:
            print('Division by zero is illegal!!')
            return
        
        return func(x,y)
    return inner_func

@smart_div
def go_divide(a,b):
    return a/b

print(go_divide(20, 2))
print(go_divide(20, 0))