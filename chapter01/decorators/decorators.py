def decorated_by(func):
    func.__doc__ += '\n Decorated by decorated_by.'
    return func

@decorated_by
def add(x,y):
    """ Return the sum of x and y"""
    return x+y


def main():
    print(add.__doc__)




if __name__ == "__main__":
    main()

