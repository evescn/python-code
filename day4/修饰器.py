def login(func):
    def inner(*args, **kwargs):
        print("passed user bingo")
        return func(*args, **kwargs)
    return inner


@login
def home():
    print("Welcome to home page!")


@login
def tv(name):
    print("Welcome %s to tv page!" %name)
    return "gmkk"


@login
def movie(name, age):
    print("Welcome %s %s to child page" %(name, age))


home()
t = tv("evescn")
print("T value ", t)
movie("evescn", 15)