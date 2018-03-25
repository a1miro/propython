from functools import wraps, partial

# no decorator - results not cached
# decorator without IP address - cached locally
# decorator with IP address - cached remotely
buffer = {}

def cache(func=None, ipaddr=None):
    
    
    if func is None:
        return partial(cache, ipaddr=ipaddr)

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not buffer.get(func, None):
            buffer[func] = {}
        params = (args, tuple([v for v in kwargs.itervalues()]))
        
        if not buffer[func].get(params, None):
            print("calling func=%s with args %s" % (func, args))
            buffer[func][params] = func(*args, **kwargs)

        return buffer[func][params]
            

    return wrapper

    
   
    
#@cache()
def add(a,b):
    return a+b

@cache 
def mul(a,b):
    return a*b

@cache(ipaddr="192.168.1.1")
def pow(e,n):
    return e**n



if __name__ == "__main__":
    add(3,5)

    print("mul(4,8)=%d" % mul(4,8))
    print("mul(5,7)=%d" % mul(5,7))
    print("mul(6,4)=%d" % mul(6,4))

    print("mul(4,8)=%d" % mul(4,8))
    print("mul(6,4)=%d" % mul(6,4))

    print("pow(2,7)=%d" % pow(2,7))
    print("pow(2,8)=%d" % pow(2,8))
    print("pow(2,10)=%d" % pow(2,10))

    print("pow(2,7)=%d" % pow(2,7))
    print("pow(2,10)=%d" % pow(2,10))


