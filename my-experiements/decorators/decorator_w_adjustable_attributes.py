'''
Created on 10 Aug 2018

@author: amironenko
'''
from functools import wraps, partial
import logging

def add_attribute(attr, value):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            setattr(func, attr, value)
            return func(*args, **kwargs)
        return inner
    return wrapper
    
@add_attribute("unittest", True)
def a():
    pass
 



if __name__ == '__main__':
    setattr(a, 'unittest', True)
    print(a.unittest)
