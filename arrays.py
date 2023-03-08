
arr = [10, 20, 30, 40, 50]
print(arr)

print('Negative index ', arr[0], arr[-1])
print('Negative index ',arr[1], arr[-2])


print('Array length', len(arr))


brands = ['Coke', 'Apple']
print(brands)
brands.append('Toyota')
print('Adding elements', brands)

colors = ['Green', 'Violet', 'Blue', 'Red', 'Yellow']
print('Colors', colors)
del colors[2]
print('Removed item with del ', colors)
colors.pop(3)
print('Removed item with pop', colors)
colors.remove('Green')
print('Removed item with remove',colors)


arr += [60, 80]
print('Concatenating 2 arrays with + operator', arr)

repeat = ['a']
print(repeat)

repeat *= 5
print('Repeat elements using * operator', repeat)

fruits = ['Apple', 'Banana', 'Grapes', 'Orange']
print(fruits)
print('Slicing [0]', fruits)
print('Slicing 2:1', fruits[2:1])
print('Slicing 3:0', fruits[3:0])

matriz = [[1,2], [3,4], [5,6]]
print('Matriz', matriz)
print('Matriz [1,2]', matriz[1][2])
print('Matriz [2,0]', matriz[2][0])