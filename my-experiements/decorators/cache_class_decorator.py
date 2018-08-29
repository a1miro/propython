'''
Created on 20 Aug 2018

@author: andrei
'''
from functools import wraps
class cache(object):
    def __init__(self, func):
        wraps(self)(func)
    
    def __call__(self, *args, **kwargs):
        print("function {} is cached".foramt(self.__wrapped__.__name__))
        return self.__wrapped__(*args, **kwargs)
    
    def __get__(self):
        #if is instance()
        pass
    

if __name__ == '__main__':
    pass