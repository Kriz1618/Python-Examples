str1 = "Str1"
print(str1)

str2 = "Str2"
print(str2)

str3 = """Str3
testing multiline string with triple quotes"""
print(str3)

str4 = '''Str4
testing multiline
string with 
triple quotes'''
print(str4)

str5 = 'Testing'
print(str5[:])
print(str5[1:4])
print(str5[:-2])

for l in str5:
    print(l, end=' ')
    

print('''Testing "interpolation way's!"''')
print('Including quote what\'s')
print("Including quote 'what\'s")
print("Including quote \"what's\"")

default_order = "{} {} and {}".format('Today', 'is', 'Friday')
print(default_order)

potitional_order = "{1} {0} and {2}".format('is', 'Today', 'Friday')
print(potitional_order)

keyword_order = "{f} {s} and {t}".format(s='is', f='Today', t='Friday')
print(keyword_order)

print("Binary representation of {0} is {0:b}".format(20))

print("Exponent representation of {0:e}".format(1281.241))

print("Two divided on three is: {0:.3f}".format(2/3))


test = "HellO pEopLe How's GoIng oN"
print(test.lower()) 
print(test.upper()) 
print(test.find('pE')) 
print(test.find('GO')) 
print(test.replace('pEopLe', 'Everybody')) 

print('Go' in test) 
print('GoIN' not in test) 
print(test.index('oN')); 
