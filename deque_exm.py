from collections import deque

def f(operations):
    d = deque()
    
    for i in operations:
        op = i.split()
        print('8', 'op', op)
        match op[0]:
            case 'append':
                d.append(op[1])
            case 'appendleft':
                d.appendleft(op[1])
            case 'extendleft':
                d.extendleft(op[1])
            case 'clear':
                d.clear()
            case 'pop':
                d.pop()
            case 'popleft':
                d.popleft()
    print(d)
                
entries = ['append 4', 'appendleft 7', 'popleft', 'append 9', 'pop']
f(entries)