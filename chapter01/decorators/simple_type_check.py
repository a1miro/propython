
def type_check_ints(decorated):
    def inner(*args, **kwargs):
        kwarg_values = [i for i in kwargs.values()]
        # Ieerate throught the args list and
        # check the type
        for arg in list(args) + kwarg_values:
            if not isinstance(arg, int):
                raise TypeError('%s only accepts integers as arguments.' %
                        decorated.__name__)

        return decorated(*args, **kwargs)

    return inner

@type_check_ints
def sum(x,y):
    return x + y

