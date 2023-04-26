import re

# print(re.compile('[A-Za-z_]', 'Alberto Style42 Rol_21'))
print(re.compile("[A-Za-z_]"       # letter or underscore
           "[A-Za-z0-9_]*"))

def validate_email_address(address):
    return print(re.match('^([a-zA-Z\d_\-]+)@([a-zA-Z\d]+)\.([a-zA-Z]{1,3})$', address)!=None)

# validate_email_address('lara@hackerrank.com')
# validate_email_address('address.com')
# validate_email_address('testing')
# validate_email_address('britts_54@hackerrank.com')

def remove_non_alphanumeric(st):
    new_st = re.sub(r'[\W_]', '', st)
    print(new_st, list(new_st), '\n')
    
# remove_non_alphanumeric('bobby !hadz@ com 123')
# remove_non_alphanumeric('Hackerrank')

def first_duplicated(word):
    charts = list(re.sub(r'[\W_]', '', word))
    dic = {}

    for chart in charts:
        if dic.get(chart):
            print(chart)
            break
        else:
            dic[chart] = True
            
first_duplicated('Hackerrank')

def first_duplicated(word):
    match = re.search(r"([a-zA-Z0-9])\1+", word)

    if match:
        print(match.group(1))
    else:
        print(-1)

first_duplicated('Hackerrank')