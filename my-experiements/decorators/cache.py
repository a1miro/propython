'''
Created on 28 Jul 2018

@author: amironenko
'''
import functools
import time
import math
from datetime import timedelta

cache_data = {}
# The cache decorator can either be with one single parameter
# @cache(max_entries = 50) or
# with no any parameter
# @cache
def cache(decorated=None, max_entries=100):
    def cached(func):
        @functools.wraps(func)
        def cache_inner(*args, **kwargs):
            if cache_data.get(func, None) == None:
                cache_data[func] = {}
            if cache_data[func].get(args, None) == None and len(cache_data[func]) < max_entries:
                cache_data[func][args] = func(*args)
            return cache_data[func][args]
        return cache_inner
    if decorated is not None:
        return cached(decorated)
    else:
        return cached

@cache
def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n*factorial(n-1)

@cache(max_entries=50)
def progression(n):
    if n == 0 :
        return 0
    if n == 1:
        return 1
    return pow(0.5,n) + progression(n-1) 
     
     

if __name__ == '__main__':
    start = time.time() 
    f = factorial(100)
    end = time.time()
    time_spend = (end - start)
    print("time = %.010f" % (time_spend))
    
    start = time.time() 
    factorial(100)
    end = time.time()
    time_spend_cached = end - start
    print("time = %.010f" % (end - start))
    
    print("time_spend/time_spend_cached = %.010f" % (time_spend/time_spend_cached))
    
    print(cache_data)
    
    
    start = time.time() 
    f = progression(100)
    end = time.time()
    time_spend = (end - start)
    print("time = %.010f" % (time_spend))
    
    start = time.time() 
    progression(100)
    end = time.time()
    time_spend_cached = end - start
    print("time = %.010f" % (end - start))
    
    print("time_spend/time_spend_cached = %.010f" % (time_spend/time_spend_cached))
    
    print(cache_data)

    
    