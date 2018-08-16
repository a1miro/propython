'''
Created on 16 Aug 2018

@author: andrei
'''
from functools import wraps

class Active:
    @classmethod
    def say1(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("say1")
            return func(*args, **kwargs)
        return wrapper
    
    def say2(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("say2")
            return func(*args, **kwargs)
        return wrapper
        
    

a = Active()

@a.say1
def func1():
    print("func1")
    
@a.say2
def func2():
    print("func2")
            
    
if __name__ == '__main__':
    func1()
    func2()