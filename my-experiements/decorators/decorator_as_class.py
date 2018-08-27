'''
Created on 26 Aug 2018

@author: amironenko
'''
import types
from functools import wraps

class Cache(object):
    def __init__(self, func):
        wraps(func)(self)
        
    def __call__(self, *args, **kwargs):
        print("__call__\n")
        return self.__wrapped__(*args, **kwargs)
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)    

    
@Cache
def standalone():
    print("standalone func call")

class Test(object):
    def __init__(self):
        pass
    @Cache 
    def test(self):
        print("Member method test \n")
        
if __name__ == '__main__':
    standalone()
    t = Test()
    t.test()
    
