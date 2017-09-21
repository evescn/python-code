def login(func):
    def inner(arg):
        print("passed user bingo")
        func(arg)
    return inner
    #return func

def home(name):
    print("Welcome %s to home page!" %name)

@login
def tv(name):
    print("Welcome to tv page!")

def movie(name):
    print("Welcome %s to movie page" %name)

@login
def child(name):
    print("Welcome %s to child page" %name)

# tv = login(tv)
# tv()
tv("evescn")


# movie = login(movie)
# movie("evescn")
# home("evescn")
#
# child("evescn")