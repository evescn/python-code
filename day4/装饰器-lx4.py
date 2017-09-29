import functools


def outer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(inner.__doc__)  # None
        return func()
    return inner


@outer
def function():
    """
    asdfasd
    :return:
    """
    print('func')


function()