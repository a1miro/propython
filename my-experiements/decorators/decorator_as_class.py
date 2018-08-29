'''
Created on 26 Aug 2018

@author: amironenko
'''
import types
from functools import wraps

class Cache(object):
    def __init__(self, param):
        '''
        if func is not None:
            wraps(func)(self)
        '''
        print("self: {}".format(self))
        print("param: {}".format(param))
    
    def __call__(self, func, *args, **kwargs):
        wraps(self)(func)
        def wrapped(*args, **kwargs):
            return self.__wrapped__(*args, **kwargs) 
        return wrapped
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)    

    
@Cache(1)
def standalone():
    print("standalone func call")

class Test(object):
    def __init__(self):
        pass
    @Cache 
    def test(self, message):
        print("Message: {}".format(message))
        
if __name__ == '__main__':
    standalone()
    t = Test()
    t.test("Hello World!")
    
