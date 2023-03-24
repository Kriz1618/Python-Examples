def exm1():
    print(1,2,3,4,5, sep='#')
    print(1,2,3,4,5, sep='*', end='&\n')

    print('First {} Second {}'.format('1', '2'))
    print('First {1} Second {0}'.format('1', '2'))

    a = []

    for i in range(1, 5):
        # print('{}{}{}'.format(''.join(a),i,''.join(a[::-1])))
        # print(f"{''.join(a)}{i}{''.join(a[::-1])}")
        # print((10**i//9)**2)
        val = 10**i
        v = val//9
        print(val, v, v**2)
        a.append(f'{i}')
        print(i * (111111111 % 10**i))
        print(111111111 % 10**i, 10**i)
        t = '1 2 3 4'
        t = list(map(int, t.split()))
        print(True if  5 in t != None else False, 5 in t )

def exm1():
    for l in 'abcdef':
        for k in [1, 2, 3, 4]:
            if l == 'c' and k == 2:
                break
            print(f'{l=} {k=}')
            
exm1()


def find_superset_array(arr: str, cases: str, ar1: str, ar2: str) -> None:
    a, n, b, c = list(map(int,arr.split())), int(cases), list(map(int, ar1)), list(map(int, ar2))
    
    res = True
    for i in range(len(b)):
        if b[i] not in a or c[i] not in a:
            res = False
            break
    print(res)

find_superset_array('1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78', '2', '1 2 3 4 5', '100 11 12')