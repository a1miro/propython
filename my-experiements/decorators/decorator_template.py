'''
Created on 26 Aug 2018

@author: amironenko
'''

from functools import wraps, partial
import time

class Cache(object):
    def __init__(self):
        self._cached = {} 
    
    def cached(self, func=None, *, lifespan=None):
        print("self: {}".format(self))
        print("func: {}".format(self))
        print("lifespan: {}".format(lifespan))
        if func is None:
            return partial(Cache.cached, self, lifespan=lifespan)
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''
            if self._cached.get((args, kwargs), None) is None:
                self._cached[(args, kwargs)] = func(*args, **kwargs)
            else:
                return self._cached[(args, kwargs)]
            '''
            print("args: {}".format(args))
        return wrapper

'''
def cached(func=None, *, lifespam=None):
    if func is None:
        return partial(cached, lifespan=lifespan)
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
'''

cache = Cache()

@cached(8)
def method0(n=0):
    time.sleep(1)
    return n + 0

@cache.cached
def method1(n=1):
    time.sleep(2)
    return n + 1

@cache.cached
def method2(n=2):
    time.sleep(3)
    return n + 2


if __name__ == '__main__':
    method0(0)
    method1(1)
    method2(2)