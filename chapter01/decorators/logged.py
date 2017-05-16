import functools
import logging
import time


def logged(method):
    """ Cause the decorated method to be run and its results logged, alonng
    with some other diagnostic information
    """
    @functools.wraps(method)
    def inner(*args, **kwargs):
        # Record our start time
        start = time.time()

        # Run the decorated method
        return_value = method(*args, **kwargs)

        # Record our completion time, and calculate the delta
        end = time.time()
        delta = end - start

        # Log the method call and the result
        logger = logging.getLogger('decorator.logged')
        logger.warn('Called method %s at %.02f; execution time % .02f'
                'seconds; result %r.' %
                (method.__name__, start, delta, return_value))
        # Return the method's origiginal return value
        return return_value
    return inner


@logged
def sleep_and_return(return_value):
    time.sleep(2)
    return return_value


def main():
    sleep_and_return(13)


if __name__ == "__main__":
    main()


