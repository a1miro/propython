'''
Created on 12 Aug 2018

@author: amironenko
'''
#p,340
from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None ):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    logname=name if name is None else func.__module__
    log=logging.getLogger(logname)
    logmsg= message if message is None else func.__name__
    
    @wraps(fun)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwarags)
    return wrapper 

if __name__ == '__main__':
    pass