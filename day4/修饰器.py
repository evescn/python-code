def login(func):
    def inner(*args, **kwargs):
        print("passed user bingo")
        return func(*args, **kwargs)
    return inner
    # return func


@login
def home():
    print("Welcome to home page!")


@login
def tv(name):
    print("Welcome %s to tv page!" %name)
    return "gmkk"

def movie(name):
    print("Welcome %s to movie page" %name)


@login
def child(name, age):
    print("Welcome %s %s to child page" %(name, age))

# tv = login(tv)
# tv()
# tv("evescn")


# movie = login(movie)
# movie("evescn")
# home("evescn")
#
# child("evescn")

home()
t = tv("evescn")
print(t)
child("evescn", 15)