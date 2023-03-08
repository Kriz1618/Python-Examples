def generator():
    for i in range(6):
        yield i*i
        
g = generator()
for i in g:
    print(i)
    
def my_generator():
    n = 1
    print('First print', n)
    yield n
    
    n += 1
    print('Second print', n)
    yield n
    
    n += 1
    print('Last print', n)
    yield n

a = my_generator()

next(a)
next(a)
next(a)