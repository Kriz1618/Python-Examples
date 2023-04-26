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