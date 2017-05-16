import functools
import json


class JSONOutputError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


def json_output(indent=None, sort_keys=False):
    """ Run the decorate function, serialize the result of that function
    to JSON, and return the JSON string.
    """

    def actual_decorator(decorated):
        @functools.wraps(decorated)
        def inner(*args, **kwargs):
            try:
                result = decorated(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                        'status': 'error',
                        'message': str(ex),
                        }
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner
    return actual_decorator


@json_output(indent=4)
def do_nothing():
    return {'status' : 'done'}



