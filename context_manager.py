def normal_code(a, b):
    file = open('file.txt', 'w')
    file.write('Testing')
    
    print(a/b)
    file.close()
    
def exepction_code(a, b):
    file = open('file.txt', 'w')
    
    try:
        file.write('Testing')
        print(a/b)
    finally:
        print('File closed')
        file.close()
        
def contex_manager(a, b):
    class onw_cm:
        def __init__(self, file, mode) -> None:
            self.file = open(file, mode)
            
        def __enter__(self):
            print(f'The entry {a, b}')
            return self.file
        
        def __exit__(self):
            print('The exit')
            self.file.close()
            
    with onw_cm('file.txt', 'w') as my_file:
        my_file.write('From own context manager')
        print('Contex Manager {}'.format(a/b))

# normal_code(4, 2)
# exepction_code(4, 0)
# contex_manager(4, 0)

from contextlib import contextmanager, AbstractContextManager

def abstract_example():
    class MyContextManager(AbstractContextManager):
        def __init__(self, resource):
            self.resource = resource

        def __enter__(self):
            # Acquire the resource and return it
            return self.resource

        def __exit__(self, exc_type, exc_value, traceback):
            # Release the resource
            self.resource.close()

# Usage example
    with MyContextManager(open("file.txt", "r")) as file:
        data = file.read()
        print('file content', data)
        
# abstract_example()

@contextmanager
def file_manager(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()
        
with file_manager('file.txt', 'a') as file:
    file.write('New line')
        
with file_manager('file.txt', 'r') as file:
    for line in file:
        print('file line', line)
        
import asyncio
from contextlib import asynccontextmanager, closing, aclosing, suppress

@asynccontextmanager
async def my_async_context_manager():
    # Async setup code
    print("Entering async context")
    await asyncio.sleep(1)
    try:
        yield "Async context object"
    finally:
        # Async cleanup code
        print("Exiting async context")
        await asyncio.sleep(1)

async def my_async_function():
    async with my_async_context_manager() as obj:
        print(f"Async context object: {obj}")
        await asyncio.sleep(1)

# asyncio.run(my_async_function())

from urllib.request import urlopen

def closing_exm(url: str) -> None:
    with closing(urlopen(url)) as page:
        for line in page:
            print(len(line))
            
# closing_exm('https://www.python.org')

def closing_file(file):
    with closing(open(file, 'r')) as file:
        for line in file:
            print(line)
            
# closing_file('file.txt')

def generator(num):
    for i in range(num):
        yield i*i
        
async def aclosing_exm():
    async with aclosing(generator(24)) as values:
        async for value in values:
            if value == 24:
                break
            else:
                print('*' * value)
                
# asyncio.run(aclosing_exm())

def suppress_exm(file):
    print('Params {}'.format(file))
    with suppress(FileNotFoundError):
        with open(file, 'r') as file:
            contents = file.read()
            print(contents)
            
def suppress_exm2(a, b):            
    with suppress(ZeroDivisionError):
        print(f'Result {a / b}')
            
# suppress_exm('file3.txt')
# suppress_exm2(2, 0)

from contextlib import redirect_stdout, redirect_stderr
import io 
import sys

def redirect_stdout_exm():
    output_buffer = io.StringIO()

    # Use redirect_stdout to redirect the output to the buffer
    with redirect_stdout(output_buffer):
        print('This will be captured in the output buffer')

    # Get the captured output from the buffer
    captured_output = output_buffer.getvalue()

    # Print the captured output
    print('Captured output:', captured_output)
    
# redirect_stdout_exm()

def foo():
    print('This is a standard output message')
    print('This is a standard error message', file=sys.stderr)

def redirect_stderr_exm():
    # Redirect stderr to a file
    with open('error.log', 'w') as f:
        with redirect_stderr(f):
            foo()
            
    with redirect_stderr(sys.stdout):
        foo()
        
# redirect_stderr_exm()

import os 
# from contextlib import chdir

# def chdir_exm(route):
#     print(f'1) Current path: {os.getcwd()}')
    
#     with chdir(route):
#         print(f'2) Current path: {os.getcwd()}')
        
#     print(f'3) Current path: {os.getcwd()}')
    
# chdir_exm('/home/kriz/Documents/React')

from contextlib import ContextDecorator, AsyncContextDecorator, ExitStack

class mycontext(ContextDecorator):
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False
    
@mycontext()
def function():
    print('The bit in the middle')

# function()

# with mycontext():
#     print('The bit in the middle')

class mycontext(AsyncContextDecorator):
    async def __aenter__(self):
        print('Starting')
        return self

    async def __aexit__(self, *exc):
        print('Finishing')
        return False
    
@mycontext()
async def function():
    print('The bit in the middle\n')

# asyncio.run(function())


async def function():
   async with mycontext():
        print('The bit in the middle2')

# asyncio.run(function())

@contextmanager
def my_context():
    print("Entering context")
    yield
    print("Exiting context")

def exitstack_exm():
    with ExitStack() as stack:
        stack.enter_context(my_context())
        print("Inside context")
        print("Second context log")
    print("Outside context")
    
# exitstack_exm()

@contextmanager
def context1():
    print("Entering context1")
    yield
    print("Exiting context1")

@contextmanager
def context2():
    print("Entering context2")
    yield
    print("Exiting context2")

def exit_multiple_stack_exm():
    with ExitStack() as stack:
        stack.enter_context(context1())
        stack.enter_context(context2())
        print("Inside contexts")
    print("Outside contexts")
    
# exit_multiple_stack_exm()

def enter_contex_exm():
    import contextlib
    
    # Define a function that opens a file and returns its contents
    def read_file(filename):
        with open(filename) as f:
            return f.read()

    # Use enter_context to open the file and read its contents
    with contextlib.ExitStack() as stack:
        f = stack.enter_context(open("file.txt"))
        contents = read_file(f)
        print(contents)

# enter_contex_exm()