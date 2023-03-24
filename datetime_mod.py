from datetime import date

def exm():
    now = date.today()
    print(now)
    
    print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
    
    birthday = date(1964, 7, 31)
    
    age = now - birthday
    
    print(age)
    print('Days: {}'.format(age.days))
    
exm()