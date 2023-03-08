tuple1 = ()
print('2', 'tuple1', tuple1)

tuple2 = (1, 2, 3)
print('5', 'tuple2', tuple2)

tuple3 = (100, 'Jonh Doe', 2100.00, 'Production')
print('8', 'tuple3 with diferent types', tuple3)

tuple4 = ('points', [1,4,3], (7,8,6))
print('11', 'tuple4', tuple4)

tuple5 = 100, 'Jonh Doe', 2100.00, 'Production'
print('14', 'tuple5', tuple5)

empCode, empName, empSalary, empDepartment = tuple5
print('17', 'fr', empCode)
print('18', 'empName', empName)
print('19', 'empSalary', empSalary)
print('20', 'empDepartment', empDepartment)

tuple6 = ('h', 'e', 'l', 'l', 'o')
print('23', 'tuple6', tuple6)
print('23', 'tuple6', tuple6[0])
print('23', 'tuple6', tuple6[1])
print('23', 'tuple6', tuple6[3])

nestedTuple = ('point', [1,2,3], (6,7,8))
print('29', 'nestedTuple', nestedTuple[0][2])
print('29', 'nestedTuple', nestedTuple[1][2])
print('29', 'nestedTuple', nestedTuple[2][2])

sliceTuple = ('h', 'e', 'l', 'l', 'o')
print('34', 'sliceTuple', sliceTuple[1:4])
print('34', 'sliceTuple', sliceTuple[:-3])
print('34', 'sliceTuple', sliceTuple[3:])
print('34', 'sliceTuple', sliceTuple[:])


tuple7 = ('h', 'e', 'l', 'l', 'o')
print('41', 'tuple7', tuple7)
tuple7 = ('r', 'e', 'a', 'd', 'y')
print('43', 'tuple7', tuple7)

tuple8 = ('h','e')
print('46', 'tuple8', tuple8)
tuple9 = ('l','l', 'o')
print('48', 'tuple9', tuple9)
print(tuple8 + tuple9)
print(('again',) * 4)

print('count', sliceTuple.count('l'))
print('index', sliceTuple.index('l'))
print('in', 'c' in sliceTuple)
print('not', 'r' not in sliceTuple)

for char in sliceTuple:
    print('58', 'char', char)
    
tuple10 = (22,11,85,96,74,31)
print(max(tuple10))
print(min(tuple10))
print(sorted(tuple10))
print(max(tuple10))