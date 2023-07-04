def exm1():
    str1 = "Str1"
    print(str1)

    str2 = "Str2"
    print(str2)

    str3 = """Str3
    testing multiline string with triple quotes"""
    print(str3)

    str4 = '''Str4
    testing multiline
    string with 
    triple quotes'''
    print(str4)

    str5 = 'Testing'
    print(str5[:])
    print(str5[1:4])
    print(str5[:-2])

    for l in str5:
        print(l, end=' ')
        

    print('''Testing "interpolation way's!"''')
    print('Including quote what\'s')
    print("Including quote 'what\'s")
    print("Including quote \"what's\"")

    default_order = "{} {} and {}".format('Today', 'is', 'Friday')
    print(default_order)

    potitional_order = "{1} {0} and {2}".format('is', 'Today', 'Friday')
    print(potitional_order)

    keyword_order = "{f} {s} and {t}".format(s='is', f='Today', t='Friday')
    print(keyword_order)

    print("Binary representation of {0} is {0:b}".format(20))

    print("Exponent representation of {0:e}".format(1281.241))

    print("Two divided on three is: {0:.3f}".format(2/3))


    test = "HellO pEopLe How's GoIng oN"
    print(test.lower()) 
    print(test.upper()) 
    print(test.find('pE')) 
    print(test.find('GO')) 
    print(test.replace('pEopLe', 'Everybody')) 

    print('Go' in test) 
    print('GoIN' not in test) 
    print(test.index('oN')); 

def exm2():
    yes_votes = 42_572_654
    no_votes = 43_132_495
    percentage = yes_votes / (yes_votes + no_votes)
    print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
    
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
        print(f'{name:10} ==> {phone:10d}')
    
    animals = 'eels'
    a = 'A'
    print(f'My hovercraft is full of {animals}.')

    print(f'My hovercraft is full of {animals!r}. {repr(animals)}')
    print(f'Test {54!s}. {a!a}')
    
    bugs = 'roaches'
    count = 13
    area = 'living room'
    print(f'Debugging {bugs=} {count=} {area=}\n')
    
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
        'Dcab: {0[Dcab]:d}'.format(table))
    
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
    
    for x in range(1, 5):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
        
    for x in range(1, 6):
        print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
        # Note use of 'end' on previous line
        print(repr(x*x*x).rjust(4))
# exm2()

def exm3():
    print('12'.zfill(5))

    print('-3.14'.zfill(7))

    print('3.14159265359'.zfill(5))
    
    import math
    print('The value of pi is approximately %5.3f.' % math.pi)
    
# exm3()

def exm4(name: str, last_name: str) -> None:
    full_name = name.title() + ' ' + last_name.title()
    print(full_name)
    
exm4('kriz', 'MARleS')