lt1 = [[1, 2, 3], [4, 5, 6], [7, 8, 8]]
lt2 = lt1
print('3', 'lt1', lt1)
print('4', 'lt2', lt2)
print('id lt1', id(lt1))
print('id lt2', id(lt2))

lt1.append([10,11, 12])
print('9', 'lt1', lt1)
print('10', 'lt2', lt2)

import copy

new_list = copy.deepcopy(lt1) 

lt1[0] = [11, 22, 33]
new_list.append([13, 14, 15])
print(f'Old list: {lt1}\nNew list: {new_list}')