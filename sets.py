def ex1():
    set1 = set([1,2,3,2])
    print('2', 'set1',type(set1), set1)

    list1 = list({11,22,33,44})
    print('5', 'list1', type(list1), list1)

    set2 = {11,55,44,22,33}
    print('8', 'set2', set2)
    set2.add(61)
    print('add', 'set2', set2)

    set2.update([88, 99, 77])
    print('13', 'set2', set2)

    set2.add(17)

    set2.update([100, 82], {14, 105, 32})
    print('16', 'set2', sorted(set2))

    set2.discard(17)
    # set2.remove(17) It'll raise an error because the item doesn't exists
    set2.remove(105)
    set2.discard(105)
    print('21', 'set2', set2)
    # set2(0) error sets can't be indexed

    print('27', 'set2', set2.pop())
    print('28', 'set2', set2)

    set2.clear()
    print('31', 'set2', set2)

    set1 = {0, 1, 2, 4, 5}
    set2 = {6, 1, 3, 2, 8}

    # union
    print(set1 | set2)
    print(set2 | set1)
    print(set2.union(set1))
    print(set1.union(set2))

    # intersection
    print(set1 & set2)
    print(set2 & set1)
    print(set2.intersection(set1))
    print(set1.intersection(set2))

    # difference
    print(set1 - set2)
    print(set2 - set1)
    print(set2.difference(set1))
    print(set1.difference(set2))

    # symetric difference
    print(set1 ^ set2)
    print(set2 ^ set1)
    print(set2.symmetric_difference(set1))
    print(set1.symmetric_difference(set2))

    print(0 in set1)
    print(6 in set1)
    print(2 in set2)
    print(10 in set2)

    for char in set('Hello'):
        print(char)
        
    print(len(set1))
    print(max(set1))
    print(min(set1))
    print(sorted(set2))

    set1 = frozenset([1, 2, 3, 4])
    set2 = frozenset([5, 6, 7, 4])

    print(set1, set2)
    print(set1.difference(set2))
    print(set1.union(set2))
    print(set1.intersection(set2))
    print(set1.symmetric_difference(set2))
    # set2.add(9)


    a = {1, 2, 3, 4}
    b = {1, 3, 5, 6}

    c, *d = a | b

    print(d)
    
    
def ex2():
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)                      # show that duplicates have been removed

    print('97', 'orange in basket', 'orange' in basket)                 # fast membership testing

    print('99', 'crabgrass in basket', 'crabgrass' in basket)


    # Demonstrate set operations on unique letters from two words

    a = set('abracadabra')
    b = set('alacazam')
    print(f'a: {a}\nb: {b}')                                 # unique letters in a

    print('108', 'a - b', a - b)                              # letters in a but not in b

    print('110', 'a | b', a | b)                              # letters in a or b or both

    print('112', 'a & b', a & b)                              # letters in both a and b

    print('114', 'a ^ b ', a ^ b )  
    
# ex2()

def ex3():
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print('120', 'a', a)
    
# ex3()

def ex3():
    A = set(map(int, '1 3 5 7 9'.split()))
    B = set(map(int, '0 2 4 6 8'.split()))
    print(A, B)
    print(A.update(B))
    
ex3()