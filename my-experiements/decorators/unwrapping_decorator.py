'''
Created on 3 Aug 2018

@author: amironenko
'''
from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y

@decorator1
def mul(x, y):
    return x * y

if __name__ == '__main__':
    print(add(3,2))
    print(add.__wrapped__(3,2))
    
    print(mul(4,3))
    print(mul.__wrapped__(4,3))
