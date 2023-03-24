import textwrap


def thinckness1():
    t = 5  # thickness
    assert t % 2 == 1
    total_width = t * 6
    ch = 'H'         # filler

    def cone(aligned_left: bool = False, pointing_down: bool = False):
        width = t * 2 - 1
        layer_gen = range(t)
        align = '>' if aligned_left else '<'
        if pointing_down:
            layer_gen = reversed(layer_gen)

        for layer in layer_gen:
            unaligned_layer = f"{ch * (1 + layer * 2): ^{width}}"
            print(f"{unaligned_layer:{align}{total_width - 1}}")

    def pillars():
        for layer in range(t + 1):
            print(f"{ch * t: ^{t*2}}{ch * t:^{total_width}}")

    def middle_belt():
        for i in range((t + 1) // 2):
            print(f"{ch * t * 5: ^{total_width}}")

    cone()  # Top Cone
    pillars()  # Top Pillars
    middle_belt()  # Middle Belt
    pillars()  # Bottom Pillars
    cone(aligned_left=True, pointing_down=True)  # Bottom Cone


def thinckness2():
    thickness = 5  # This must be an odd number
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    # Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) +
              (c*thickness).center(thickness*6))

    # Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    # Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) +
              (c*thickness).center(thickness*6))

    # Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c +
              (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


test = 'abcdefghijklimnoqrstuvwxyz'


def wrap1(string, width):
    res = ''
    for i in range(0, len(string), width):
        print(i, string[i:i+width])
        res += string[i:i+width] + '\n'
    print(res)

# wrap1(test, 5)


def wrap(string, max_width):
    return textwrap.fill(string, max_width)

# wrap(test,4)


def merge_the_tools(string, k):
    for part in zip(*[iter(string)] * k):
        print('77', 'part', part)
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d]))

# merge_the_tools('AABCAAADA',3)


print(3 // 2)


def door_mat(N, M):
    design_num = 0

    for x in range(N + 1):
        if x < (N // 2):
            print(('.|' + ('..|' * design_num) + '.').center(M, '-'))
            design_num += 2

        elif x == (N//2 + 1):
            print(('WELCOME').center(M, '-'))

        elif x > (N//2 + 1):
            design_num -= 2
            print(('.|' + ('..|' * design_num) + '.').center(M, '-'))

# door_mat(7, 21)

wd = 'hello   world  lol'
result = wd
wd_list = wd.split()

for i in wd_list:
    word = i[:1].upper() + i[1:] + ' '
    result = result.replace(i, word)

# print('121', 'result', result)

def print_formatted(number):
    n = len(bin(number+1)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(n), oct(i)[2:].rjust(n), hex(i)[2:].rjust(n), bin(i)[2:].rjust(n))
        

def print_formatted1(number):
    W = len(f'{number:b}')
    print(W)
    [print(f'{i:{W}d} {i:{W}o} {i:{W}X} {i:{W}b}') for i in range(1,number+1)]
        
# print_formatted1(12)

def rangoli(num):
    abc = 'abcdefghijklimnoqrstuvwxyz'
    width = 1 + (num - 1) * 4
    abc_list = abc[:num]
    rang = (num * 2) - 1
    limit = num-1
    print('rang',rang)
    for i in range(0, rang):
        m = abc_list[limit:]
        fr = list(m[1:])
        fr.reverse()
        m = fr + list(m) if i > 0 else m
        print('-'.join(m).center(width, '-'))
        limit = limit - 1 if i < rang // 2 else limit + 1


def print_rangoli(size):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    s = (size-1) * 4 + 1
    r = list(range(1, size+1)) + list(range(1, size+1))[:-1][::-1]

    for i in r:
        l = list(reversed([alph[s] for s in range(size-i, size)]))
        print('-'.join(l+ l[: i*2-3][:i-1][::-1]).center(s, '-'))

# rangoli(6)
# print_rangoli(6)

from itertools import permutations

arr = set([''.join(sorted(list(x))) for x in list(permutations('KRIZ',2))])
# print(sorted(list(permutations('KRIZ',2))))

# A, B = ['test', 5]

# print('169', 'A, B', A, B)

def permu(string, width):

    for i in range(int(width)):
        result = sorted(list(set([''.join(sorted(list(x))) for x in list(permutations(string, i+1))])))
        for j in result:
            print(j)

# permu('SENDING', 5)

import cmath
import math

def polar_coordinates(num):
    c = complex(num)
    a = c.real
    b = c.imag
    print(math.sqrt(a**2+b**2))
    print(cmath.phase(complex(a,b)))
    
    
def polar(num):

    z = complex(num)
    r, phi = cmath.polar(z)
    print(r)
    print(phi)

# polar_coordinates(1+2j)
# polar(1+2j)    
