def ex1():
    numerator = int(input('Type a numerator: '))
    denominator = int(input('Type a denominator: '))

    try:
        res = numerator / denominator
        # raise ZeroDivisionError
        print(f"{numerator} divided into {numerator} is euqal to: {res}")
    except ZeroDivisionError:
        print('Division cannot be performed')
    finally:
        print('Execution fulfilled!!')
    
def err_ex():
    try:
        """
        This code will arise an exception
        """
        a = 'hi'
        b = int(a)
    except:
        print('Exception caught!')
        
# ex1()
# err_ex()

def ex2():
    try:
        raise TypeError
    except TypeError:
        print('TypeError Exception caught!')
        
# ex2()

def ex3():
    try:
        a = int(input('Type the first number: '))
        b = int(input('Type the second number: '))
        
        if a < 0:
            raise TypeError
        
        c = a/b
        print("{} / {} = {}".format(a, b, c))
    except ZeroDivisionError:
        print('Division by zero is invalid')
    except ValueError:
        print('Data types are invalid')
    except TypeError:
        print('Value is not in range')
    
# ex3()

class CustomExcept(Exception):
    def __init__(self):
        super()

def ex4():
    try:    
        age = int(input('Type your age: '))
        if age < 18:
            raise CustomExcept
    except ValueError:
        print('Invalid data type')
    except CustomExcept:
        print('Age is less than 18')
    else:
        print('Age is greater than or equal to 18')
    finally:
        print('End')
     
ex4()
    
    
    
    
    
    
    
    
    
    
    
    