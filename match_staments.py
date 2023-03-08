def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 402 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(404))
print(http_error(418))

def exam1(x, y):
    match x, y:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
        
exam1(10, 0)
exam1(0, 5)

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

def exam2():
    color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")
            
exam2()