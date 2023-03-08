def lonelyinteger(a):
    sorted_arr = sorted(a)
    current = sorted_arr[0]
    i = 1

    while i < len(sorted_arr) - 1:
        next_val = sorted_arr[i + 1] if sorted_arr[i + 1] is not None else None

        if current != next_val and next_val is None:
            return current
        elif  current == sorted_arr[i]:
            current = next_val
            i += 2
        else:
            i += 1
    return current

a = [34,95,34,64,45,95,16,80,80,75,3,25,75,25,31,3,64,16,31]

# res = lonelyinteger(a)

# print('19', 'res', res)

entry = str('testing')
entry_list = list(entry)
mo = entry[:2]
entry.replace("te", '')
del entry_list[:2]
# entry.split(2)

print('28', 'mo', mo, entry_list, entry.lower())
entry_list.append(mo)
print('32', 'entry_list', ''.join(entry_list))

print('R' in 'nelkas')
print('nelkas'.index('k'))

test = 'abcdefghijklmnopqrstuvwz'

for i in range(6):
    char = test[0]
    test = test[1:] + char
print('43', 'test', test)

arr = [1,5,6]

arr.insert(1,3)
print('48', 'arr', arr)

def minion_game(string):
    vowels = 'AEIOU'
    str_lenght = len(string)
    kevin, stuart = 0, 0

    for i in range(str_lenght):
        if string[i] in vowels:
            kevin += (str_lenght - i)
        else:
            stuart += (str_lenght - i)

    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")
        
minion_game('BANANA')


string = 'Tessing'

print(string[:3] + 't' + string[4:])

print(max(sorted(list('dbace'))))

print('a' < 'b', 'f' < 'c')

lt = ['r', 's', 't']

res = lt + list('xyz')
res += list('wres')

print(res)


def gridChallenge(grid):
    sorted_grid = []
    for row in grid:
        sorted_row = sorted(row)
        sorted_grid.append(sorted_row)
    res = "YES"
    columns = [list(column) for column in zip(*sorted_grid)]
    for column in columns:
        if column != sorted(column):
            res = "NO"
            break
    return res

grid = ['mpxz', 'abcd', 'wlmf']

print('Grid', gridChallenge(grid))

print(grid, zip(*grid))


# class MyQueue(object):
#     def __init__(self):
#         self.q1 = []
#         self.q2 = []
    
#     def peek(self):
#         if not self.q2:
#             while self.q1:
#                 self.q2.append(self.q1.pop())
         
#         return self.q2[-1]
        
#     def pop(self):
#         if not self.q2:
#             while self.q1:
#                 self.q2.append(self.q1.pop())
        
#         return self.q2.pop()
        
#     def put(self, value):
#         self.q1.append(value)

# queue = MyQueue()
# t = int(input())
# for line in range(t):
#     values = map(int, input().split())
#     values = list(values)
#     if values[0] == 1:
#         queue.put(values[1])        
#     elif values[0] == 2:
#         queue.pop()
#     else:
        # print(queue.peek())
        
        
def fun_list():
    arr = [x for x in range(1, 6,2)]
    arr1 = arr
    arr1.append(10)
    return *arr,

print(fun_list())