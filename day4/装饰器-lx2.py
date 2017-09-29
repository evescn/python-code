def before1(*request, **kargs):
    print("Before")


def after1(*request, **kargs):
    print("After")


# def Filter(before_func, after_func):
#     def login(main_func):
#         def inner(*args, **kwargs):
#             before_func()
#             print("passed user bingo")
#             main_func(*args, **kwargs)
#             after_func()
#             # return func(*args, **kwargs)
#         return inner
#         # return func
#     return login


def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(*request, **kargs):
            before_result = before_func(*request, **kargs)
            if (before_result != None):
                return before_result

            main_result = main_func(*request, **kargs)
            if (main_result != None):
                return main_result

            after_result = after_func(*request, **kargs)
            if (after_result != None):
                return after_result
        return wrapper
    return outer


@Filter(before1, after1)
def home():
    print("Welcome to home page!")


@Filter(before1, after1)
def tv(name):
    print("Welcome %s to tv page!" %name)
    return "gmkk"


def movie(name):
    print("Welcome %s to movie page" %name)


@Filter(before1, after1)
def child(name, age):
    print("Welcome %s %s to child page" %(name, age))


home()
t = tv("evescn")
print(t)
child("evescn", 15)