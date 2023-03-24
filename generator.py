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

# a = my_generator()

# next(a)
# next(a)
# next(a)

def generator_expression():
    generator = (num ** 2 for num in range(10))
    for num in generator:
        print(num)
        
generator_expression()

       
import time

class iterate_lists():
    def __init__(self, exponent) -> None:
        self.exp = exponent
        t1 = time.process_time()
        self.with_list()
        t2 = time.process_time()
        self.with_generators()
        t3 = time.process_time()
        self.with_generators2()
        t4 = time.process_time()
        
        print('Time with list {}'.format((t2 - t1)/1000))
        print('Time with generators {}'.format((t3 - t1)/1000))
        print('Time with generators2 {}'.format((t4 - t1)/1000))
        
        
    def with_list(self):
        l = []
        for x in range(1000000):
            l.append(x ** self.exp)
    
    def with_generators(self):
        for x in range(1000000):
            yield x ** self.exp
            
    def with_generators2(self):
        yield [x ** self.exp for x in range(1000000)]
        
iterate_lists(3)