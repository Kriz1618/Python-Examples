
import datetime
import decimal


print('isalnum abc123', 'abc123'.isalnum())
print('isalnum abc123$', 'abc123$'.isalnum())

print('isalpha abcD', 'abcD'.isalpha())
print('isalpha abcd1', 'abcD1'.isalpha())

print('isdigit 1234', '1234'.isdigit())
print('isdigit 1234abc', '1234abc'.isdigit())
print('contains isdigit 1234abc', any(i.isdigit() for i in '1234abc'))

print('isupper ABCD123#', 'ABCD123#'.isupper())
print('isupper Abcd123#', 'Abcd123#'.isupper())

print('islower abcd123#', 'abcd123#'.islower())
print('islower Abcd123#', 'Abcd123#'.islower())

name = "Fred"
print(f"He said his name is {name!r}.")
print(f"He said his name is {repr(name)}.")

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")

# today = datetime.datetime(year=2017, month=1, day=27)
today = datetime.datetime.now()
print(f"{today:%B %d, %Y}")
print(f"{today=:%B %d, %Y}")

number = 1024
print(f"{number:#0x}")

foo = "bar"
print(f"{ foo = }")

line = "The mill's closed"
print(f"{line = }")
print(f"{line = :20}")
print(f"{line = !r:20}")

newline = ord('\n')
print(f"newline: {newline}")


def dates_diff(a, b):
    t_a = datetime.datetime.strptime(a, "%a %d %b %Y %X %z")
    t_b = datetime.datetime.strptime(b, "%a %d %b %Y %X %z")
    print('Dates diff', abs(int((t_a - t_b).total_seconds())))
    
# dates_diff('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000')

print('C:\some\name')
print(r'C:\some\name')

st = 'maRca'
r = st[:2] + 'Z' + st[3:]
print(st, r)