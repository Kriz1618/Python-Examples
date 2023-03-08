import math

def exa1():
    num = [9, 36, 49, 81, 121]

    x = list(map(math.sqrt, num))

    print(x)
    
# exa1()

def exa2():
    num = (6, 9, 21, 44)

    resu = map(lambda i: i + i, num)

    print(list(resu))
    
# exa2()

def exa3():
    set_exm = {33, 102, 62, 96, 44, 28, 227}
    
    upd_itms = map(lambda x : x%3, set_exm)
    print(upd_itms)

    print(set(upd_itms))
    
# exa3()

def custom_map(func, iterables):
    # Create an empty list to hold the results
    result = []
    # Apply the function to each element in the iterable
    for element in iterables:
        result.append(func(element))
    # Return the new iterable
    return result 

def square(x):
    return x**2

# Define the iterable to be mapped over
my_list = [1, 2, 3, 4, 5]

# Call custom with the function and iterable
result = custom_map(lambda x : x**2, my_list)

# Print the result
print(result)