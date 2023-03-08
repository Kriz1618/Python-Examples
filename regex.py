import re 

my_txt = 'freeCodeCamp'
my_regex_1 = '^freecodecamp$'

res = re.match(my_regex_1, my_txt)
# print(res)

if re.search('tes', 'This is a search test'):
    print('search test')
res = re.match(my_regex_1, my_txt, re.IGNORECASE)
# print(res)

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'
my_regex = 'friday'

res = re.search(my_regex, my_txt, re.IGNORECASE)
# print(res)

res = re.search(my_regex, my_txt, re.IGNORECASE)
# print("The first occurrence is located between index", res.start(), "and index", res.end())

res = re.findall('te.', 'testing findall func with a string  text')
print('24', 'res', res)

my_txt = 'Every friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'
my_regex = 'friday'
res = re.findall(my_regex, my_txt, re.IGNORECASE)

# print(res)

animals = 'Cat rat mat fat pat dog'
filteredAnimals = re.findall("[c-mC-M]at", animals)
for i in filteredAnimals:
    print(i)
filteredAnimals = re.findall("[^Cr]at", animals)
for i in filteredAnimals:
    print(i)
my_txt = "Python and JavaScript and C# and Java and Golang and F#"
my_regex = 'and'

res = re.split(my_regex, my_txt)
# print(res)

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'
my_regex = 'friday'

res = re.sub(my_regex, "Monday", my_txt, 4, re.IGNORECASE)
# print(res)

digits = '12345t6'
print('Matches: ', len(re.findall("\d", digits)))

print('Matches2: ', re.search('\d{5}', digits))
print('Matches3: ', len(re.findall('\d{5,6}', '123 12345 123456 1234567')))
print('Phone number check', re.search('\w{3}-\w{3}-\w{4}', '412-555-1212'))
print('Name check', re.search('\w{2,20}', 'Alberam'))
print('Name check', re.search('\w{2,20}', '451y98'))
print('Name check', re.search('\w{2,20}\s\w{2,20}', '451y98'))
print('Name check', re.search('\w{2,20}\s\w{2,20}', 'Kriz Marles'))

print('Matches', len(re.findall('a+', 'Kriz Marles as a software engineer')))
print('Matches', re.findall('a+', 'Kriz Marles as a software engineer'))
