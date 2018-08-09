'''
Created on 9 Aug 2018

@author: andrei
'''
from functools import wraps

registered = []
cached = []

def register(cache=False):
        
    def decorator(func):
        registered.append(func)
        if cache:
            cached.append(func)
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
        
@register(True)
def func1():
    print("func1")
        
@register(False)
def func2():
    print("func2") 
    
@register(True)
def func3():
    print("func3")
    print(func3.__name__)     
    
@register
def func4():
    print("func4")  
    print(func4.__name__)     
 
        
if __name__ == '__main__':
    func1()
    func2()
    func3()
    
    print(registered)
    print(cached)