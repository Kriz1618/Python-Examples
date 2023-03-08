def exm1():
    new_dict = {1: 'Hello', 2: 'Hi', 3: 'Hola'}
    print(new_dict.get(8))
    print(new_dict[1])
    print(new_dict.get(2))

    new_dict[1] = 'Hey'
    print(new_dict)

    new_dict[4] = 'Namaste'
    print(new_dict)

    new_dict[6] = 'niho'
    print(new_dict)

    squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    print(squares)

    del squares[1]
    print(squares)

    squares = {x: x*x for x in range(1, 6)}
    print('generated with for', squares)

    print(1 in squares)
    print(2 not in squares)

    print(4 in squares)

    for i in squares:
        print(f"i {i}", squares[i], squares.get(i))

    print(len(squares))

    print(sorted(squares))


def exm2():
    people = {
        1: {'name': 'Jonh', 'age': '27', 'sex': 'Male'},
        2: {'name': 'Edith', 'age': '17', 'sex': 'Female'}
    }
    people[3] = {}
    people[3]['name'] = 'Moon'
    people[3]['age'] = '22'
    people[3]['sex'] = 'Female'
    people[3]['married'] = 'No'
    print(people.items())
    
    for id, info in people.items():
        print('\nPerson Id:', id)
        
        for key in info:
            print(f"{key}: {info[key]}")
    
 
# exm2()

def sort_dictionaries(dic):
    res = sorted(dic, key = lambda k: (dic[k], k))
    print('Original: {}\n Sorted: {}'.format(dic,res))

# sort_dictionaries({'Naldo': 3, 'Bill': 4, 'Alex' : 4, 'Bob' : 3, "Charles": 7})


def iterate_dict():
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

    # Strategy:  Iterate over a copy
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]
    print(users)        
    # Strategy:  Create a new collection
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status
    print(active_users)       
# iterate_dict()

def ex2():
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    print('85', 'tel', tel)

    print('87', '\'tel[\'jack\']', tel['jack'])

    del tel['sape']
    tel['irv'] = 4127
    print('91', 'tel', tel)

    print('93', 'list(tel)', list(tel))

    print('95', 'sorted(tel)', sorted(tel))

    print('97', 'guido in tel', 'guido' in tel)

    print('jack' not in tel)
# ex2()

def ex3():
    print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
    
    print({x: x**2 for x in (2, 4, 6)})
    
    print(dict(sape=4139, guido=4127, jack=4098))
    
ex3()

def looping():
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)
    print('\n')
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))
        
# looping()

def enumerating():
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)
        
def ex3():
    print('Reverse')
    for i in reversed(range(1, 10, 2)):
        print(i)
        
        print('Sorted')
        basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
        for i in sorted(basket):
            print(i)

        print('\nEliminating duplicates')
        basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
        for f in sorted(set(basket)):
            print(f)

# enumerating()       
# ex3()

def ex4():
    import math
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)

    print('153', 'filtered_data', filtered_data)