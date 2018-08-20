'''
Created on 29 Jul 2018

@author: amironenko
'''
import types
from functools import wraps
import time

class One(object):
    def __init__(self):
        pass
    
    class cached(object):
        def __init__(self, decorated):
            wraps(decorated)(self)
            self._decorated = decorated 
            self._cache={}
            
        def __call__(self, *args, **kwargs):
            if self._cache.get(self._decorated, None) is None:
                self._cache[self._decorated] = {}
            if self._cache[self._decorated].get((args), None) is None:
                self._cache[self._decorated][(args)] = self._decorated(*args)
            return self._cache[self._decorated][(args)] 
        
        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                return types.MethodType(self, instance)
    
    @cached
    def method0(self, n=0):
        time.sleep(1)
        return n + 0
    
    @cached
    def method1(self, n=1):
        time.sleep(2)
        return n + 1
    
    @cached
    def method2(self, n=2):
        time.sleep(3)
        return n + 2


       
'''        
class Raspberry(One):
    def __init__(self):
        super(Raspberry,self).__init__()
    
    def r]un_all(self):
        self.method0()
        self.method1()
        self.method2()
        print(self._cache)
                
    @cache
    def method0(self, n=0):
        return n

    #@cache
    def method1(self, n=1):
        return n

    #@cache
    def method2(self, n=2):
        return n
'''
    
if __name__ == '__main__':
    reg = One()
    start = time.time() 
    reg.method0()
    end = time.time()
    time_spend = (end - start)
    print("method0 time = %.010f" % (time_spend))
    
    start = time.time() 
    reg.method1()
    end = time.time()
    time_spend = (end - start)
    print("method1 time = %.010f" % (time_spend))
    
    start = time.time() 
    reg.method2()
    end = time.time()
    time_spend = (end - start)
    print("method2 time = %.010f" % (time_spend))
   
    start = time.time() 
    reg.method0()
    end = time.time()
    time_spend = (end - start)
    print("method0 time = %.010f" % (time_spend))
    
    start = time.time() 
    reg.method1()
    end = time.time()
    time_spend = (end - start)
    print("method1 time = %.010f" % (time_spend))
    
    start = time.time() 
    reg.method2()
    end = time.time()
    time_spend = (end - start)
    print("method2 time = %.010f" % (time_spend))
    
    
    