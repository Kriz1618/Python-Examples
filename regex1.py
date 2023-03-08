import re

# print(re.compile('[A-Za-z_]', 'Alberto Style42 Rol_21'))
print(re.compile("[A-Za-z_]"       # letter or underscore
           "[A-Za-z0-9_]*"))