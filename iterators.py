# while
i = 5
while(i>0):
    print(i)
    i -=1
    
lis = [55, 44, 88, 77]

iterator = iter(lis)

# print(next(iterator))
# print(next(iterator))
# print(iterator.__next__())
# print(iterator.__next__())

class Pow_of_Two:
    ''' Class that implements a   customized 
    iterator of powers of two'''
    
    def __init__(self, max = 0):
        self.max = max
        
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
        
# print('35', 'Pow_of_Two.__doc__', Pow_of_Two.__doc__)
# a = Pow_of_Two(4)
# i = iter(a)
# print(next(i))
# print(next(i))
# print(next(i))

# class Infinige_Iter:
#     ''' Class that implements a customized 
#     iterator of infinite'''

#     def __iter__(self):
#         self.num = 1
#         return self
    
#     def __next__(self):
#         num = self.num
#         self.num += 2
#         return num
       
        
# print('35', 'Infinige_Iter.__doc__', Infinige_Iter.__doc__)
# i = Infinige_Iter()
# a = iter(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

def g():
    yield 1
    yield 2
    yield 3


gen = g()

print(next(gen))

my_list = list(gen)

first_2 = my_list[:2]
print(first_2)