
def exam1(s):
    letters = []

    for letter in s:
        print('6', 'letter', letter)
        letters.append(letter)
    print("Examp1: {letters}", letters)


def exam2(s):
    letters = [letter for letter in s]
    print('Examp2:\b {}'.format(letters))


def exam3(s):
    letters = list(map(lambda x: x, s))
    print(f"Examp3: {letters}")


# exam1('test1')
# exam2('test2')
# exam3('test3')

def examp4():
    lt = ['Event' if i % 2 == 0 else 'Odd' for i in range(10)]
    print(lt)


def examp5():
    matriz = [[1, 2], [3, 4], [5, 6], [7, 8]]
    transpose = [[row[i] for row in matriz] for i in range(2)]
    print(f'Original: {matriz}\nTransposed {transpose}')

# examp4()
# examp5()


def examp6():
    lt = [1, 2]
    print('original ', lt)

    lt.append(3)
    print(f'append 3 {lt}')

    lt.extend(x for x in range(4, 6))
    print(f'extend from 4 to 5 {lt}')

    lt.insert(0, 0)
    lt.insert(len(lt), 6)
    print(f'inserted 0 at the begining and 6 at the end {lt}')

    lt.append(0)
    lt.remove(0)
    print(f'remove the first occurs of 0 {lt}')

    lt.pop(0)
    lt.pop(-1)
    print(f'remove an element at the position 0 and -1')

    lt1 = lt.copy()
    print(f'copied the list conetnt to the list lt1 {lt1}')

    lt.clear()
    del lt[:]
    print(f'removed all items from the lt list {lt}')

    print(f'index of the value 5: {lt1.index(5)}')
    print(f'index of the value 5 in the range 2-4: {lt1.index(5, 2, 4)}')

    lt1.append(2)
    print(f'counted how many times is the value 2 in lt1: {lt1.count(2)}')

    lt1.sort(key=None, reverse=True)
    print(f'sorted and reverse lt1: {lt1}')

# examp6()


def examp7():
    """Using list as stacks"""
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print('81', 'stack', stack)

    stack.pop()

    print('85', 'stack', stack)

    stack.pop()

    stack.pop()

    print('91', 'stack', stack)

# examp7()


def examp8():
    """Using list as queues"""
    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")           # Terry arrives
    queue.append("Graham")          # Graham arrives
    queue.popleft()                 # The first to arrive now leaves

    queue.popleft()                 # The second to arrive now leaves

    # Remaining queue in order of arrival
    print('106', 'queue', queue)

# examp8()


def exmap9():
    lt1, lt2, lt3 = [], [], []
    for x in range(10):
        lt1.append(x**2)

    lt2 = list(map(lambda x: x**2, range(10)))

    lt3 = [x**2 for x in range(10)]

    print(f'lt1: {lt1}\nlt2: {lt2}\nlt3: {lt3}\n')

    t1, t2 = [], []
    t1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                t2.append((x, y))

    print(f't1: {t1}\nt2: {t2}\n')

# exmap9()


def ex1():
    vec = [-4, -2, 0, 2, 4]
    # create a new list with the values doubled
    print([x*2 for x in vec])

    # filter the list to exclude negative numbers
    print([x for x in vec if x >= 0])

    # apply a function to all the elements
    print([abs(x) for x in vec])

    # call a method on each element
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    print([weapon.strip() for weapon in freshfruit])

    # create a list of 2-tuples like (number, square)
    print([(x, x**2) for x in range(6)])

# ex1()


def ex2():
    from math import pi
    print([str(round(pi, i)) for i in range(1, 6)])


ex2()


def ex3():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    
    print(f'original: {matrix}\ntransposed: {[[row[i] for row in matrix] for i in range(4)]}')
    transposed = []
    
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    print('181', 'transposed', transposed)
    transposed.clear()
    
    for i in range(4):
    # the following 3 lines implement the nested listcomp
        transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)
    print('190', 'long way transposed', transposed)
    
    print('short way', list(zip(*matrix)))
# ex3()

def del_st():
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    print('198', 'a', a)

    del a[2:4]
    print('201', 'a', a)

    del a[:]
    print('204', 'a', a)
del_st()