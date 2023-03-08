def ex1():
    t = 12345, 54321, 'hello!'
    print('3', 't[0]', t[0])

    print('5', 't', t)

    # Tuples may be nested:
    u = t, (1, 2, 3, 4, 5)
    print('9', 'u', u)

    # Tuples are immutable:
    # t[0] = 88888


    # but they can contain mutable objects:
    v = ([1, 2, 3], [3, 2, 1])
    print('17', 'v', v)
    
    a, b, c = t
    print(f'unpacking {a, b, c}')
    
ex1()

def ex2():
    empty = ()
    singleton = 'hello',    # <-- note trailing comma
    print('24', 'len(empty)', len(empty))

    print('26', 'len(singleton)', len(singleton))

    print('28', 'singleton', singleton)
    
# ex2()