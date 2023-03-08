from math import *

print(ceil(235.1423))
print(floor(235.1423))

print(factorial(3))

print(max(5, 8, 4, -8, 10))
print(min(5, 8, 4, -8, 10))

print(5^2)
print(5**2)
print(pow(5, 2))

print(8%3)

print(abs(41 * -1))

print(sqrt(25))

val1 = 100
print(type(val1))
print(isinstance(val1, int))
print(isinstance(val1, float))
print(isinstance(val1, complex))

val2 = 100.24
print(type(val2))
print(isinstance(val2, int))
print(isinstance(val2, float))
print(isinstance(val2, complex))

val3 = 100 + 6j
print(type(val3))
print(isinstance(val3, int))
print(isinstance(val3, float))
print(isinstance(val3, complex))

print(0b1101)
print(0xab)
print(0o23)

print(10 + 33.4)

print(int(10.5))
print(int(-20.15))
print(float(15))


from decimal import Decimal as D
print(0.2)
print(D(0.2))

from fractions import Fraction as F
print(F(1.5))
print(F(5))
print(F(1,5))
d1 = 0.1 + 0.2
print(d1) 
d1 = 1.20 * 2.5
print(d1)
print(D(0.1) + D(0.2))
print(D(1.2) * D(2.5))

import math
print(math.pi)
print(math.cos(10))
print(math.log(10))
print(math.log10(10))
print(math.exp(10))
print(math.factorial(5))
print(math.sinh(10))
print(abs(-74.12))

import random
print('Random ', random.randrange(5,15))
print('Random ', random.randrange(5,15))
print('Random ', random.randrange(5,15))
print('Random ', random.randrange(5,15))

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
print(random.choice(days))
print(random.choice(days))

print(days)
random.shuffle(days)
print(days)

print(random.random())