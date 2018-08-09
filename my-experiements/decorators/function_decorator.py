'''
Created on 27 Jul 2018

@author: amironenko
'''

import random
import functools
import sys

functions = []
funcs = []

def echo(func):
    return func

def logging(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("{0}:args:{1}, kwargs:{2}".format(func.__name__,args, kwargs))
        return func(*args, **kwargs)
    return inner 

def register(func):
    functions.append(func)
    return func

@register
@logging
def method1(a=1):
    return a;

@register
@logging
def method2(a=2):
    return a;

@register
@logging
def method3(a=3):
    return a;

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        #raise Exception("Must be using Python3!")
        pass
    
    
    print("{0}!={1}".format(10,factorial(10)))
   
     
    results = []
    i = 1
    result = 0
    print(functions)
    for f in functions:
        result = f(i)
        results.append(result)
        i += 1
    print(results)
   

 
    
