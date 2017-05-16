import functools
import json

def json_output(decorated):
    """ Run the decorated function, serialize the result of that function
    to JSON, and return the JSON string.
    """

    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        result = decorated(*args, **kwargs)
        return json.dumps(result)
    return inner


@json_output
def do_nothing():
    return {'status':'done'}

def main():
    print(do_nothing())

if __name__ == "__main__":
    main()

