def greeting(name: str) -> str:
    return 'Hello ' + name

Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

from collections.abc import Sequence

def sec_exam():
    ConnectionOptions = dict[str, str]
    Address = tuple[str, int]
    Server = tuple[Address, ConnectionOptions]
    
    def broadcast_message(message: str, servers: Sequence[Server]) -> None:
        ...
    # or
    def broadcast_message(
        message: str,
        servers: Sequence[tuple[tuple[str, int], dict[str, str]]]) -> None:
        ...
 
from typing import NewType

UserId = NewType('UserId', int)

def new_type():
    some_id = UserId(524313)
    print('UserId', type(some_id))

def derived_newtype():
    ProUserId = NewType('ProUserId', UserId)
    some_id = ProUserId(524313)
    print('ProUserId', type(some_id))
    
if __name__ == '__main__':
    # print(greeting('Jonh Doe'))
    # print(greeting(5))
    
    # print(scale(2.0, [1.0, -4.2, 5.4]))
    new_type()
    derived_newtype()
    
def process_items(items: list[str]):
    for item in items:
        print(item)
        
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

def process_item(item: int | str):
    print(item)
    
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
        
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name