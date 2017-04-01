import functools


class User(object):
    """ A representation of a user in our app."""

    def __init__(self, username, email):
        self.username = username
        self.email = email

class Anonymous(User):
    """ An anonymous user; a stand-in for an actual user
    that nontheless is not an actual users.
    """

    def __init__(self):
        self.username = None
        self.email = None


    def __nonzero__(self):
        return False



def requires_user (func):
    @functools.wraps(func)
    def inner(user, *args, **kwargs):
        """ Verify """
