string_e = 'Kr'
int_e = 6
float_e = 10.3
boolean_e = False
new_num = int_e + float_e

print(string_e, type(string_e))
print(int_e, type(int_e))
print(float_e, type(float_e))
print(boolean_e, type(boolean_e))
print(new_num, type(new_num))
# print(string_e + int_e) error
print(string_e + str(int_e))