'''
Created on 10 Aug 2018

@author: amironenko
'''
from functools import wraps, partial
import logging

def add_attribute(attr, value):
    def wrapper(func):
        setattr(func, attr, value)
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return wrapper
    
@add_attribute("unittest", True)
def a(text):    
   print(text) 

if __name__ == '__main__':
    print(a.unittest)
