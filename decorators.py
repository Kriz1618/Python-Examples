# doc https://book.pythontips.com/en/latest/decorators.html
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

# print(go_divide(20, 2))
# print(go_divide(20, 0))

def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")

# a_function_requiring_decoration()
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# a_function_requiring_decoration()

# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")

# a_function_requiring_decoration()
# print(a_function_requiring_decoration.__name__)

from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

# print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
# print(func())
# Output: Function is running

can_run = False
# print(func())
# Output: Function will not run

# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username, auth.password):
#             authenticate()
#         return f(*args, **kwargs)
#     return decorated

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


# result = addition_func(4)
# print(result)

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    print('hi')
    pass

# myfunc1()
# Output: myfunc1 was called
# A file called out.log now exists, with the above string

@logit(logfile='func2.log')
def myfunc2():
    pass

# myfunc2()

from datetime import datetime
from functools import wraps

def log_exc_time(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        print(f'function {func.__name__} executed at {datetime.now()}')
        return func(*args, **kwargs)
    return decorated

@log_exc_time
def is_odd(num: int) -> None:
    print('The number {} {} an odd'.format(num, 'is' if num % 2 != 0 else 'isn\'t'))
    
is_odd(7)


class logit(object):

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self._logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()

        # return base func
        return self.func(*args)



    def notify(self):
        # logit only logs, no more
        pass
    
logit._logfile = 'out2.log' # if change log file
@logit
def myfunc1():
    pass

# myfunc1()