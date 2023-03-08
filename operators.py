
""" 
  arithmetic operators
"""
su = 4+5
print('Add 4 to 5', su)
re = 9 - 4
print('Rest 9 - 4', re)
ne = -8
print('Negative ', ne)
mu = 3*4
print('3 * 4', mu)
po = 2**3
print('2^3', po)
div = 5/2
print('5 / 2', div)
die = 5//2
print('result without residue 5 / 2 =>', die)
mod = 5 % 2
print(mod)

# relational
print('==', 12 == mu)
print('>', 9 > 11)
print('<', 4 < 5)
print('<=', 4 <= 5)
print('>=', 3 >= 4)

# logics
print('and', div < 5 and 2 == 2)
print('or', (div < po) or (mod > div))
print('not', not(div < po) or (mod > div))

# assignation
c = 1
c += 7
c -= 4
c *= 4
c /= 2
c **= 2
c %= 3

print(c)
