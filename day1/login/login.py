import sys

lock = "lock.txt"
logfile = "login.txt"
login_info = 0
i = 0

while i < 3 and login_info== 0 :
    name = input("Please input your name: ")

    f = open(lock, "r")
    for line in f.readlines():
        # if name in line:
        if name == line.strip():
            f.close()
            sys.exit('\033[32:1m用户 %s 已经被锁定\033[0m' % name)

    password = input("Please input password: ")

    f = open(logfile, "r")
    for line in f.readlines():
        user_file, pass_file = line.split()
        if user_file == name and pass_file == password:
            print("Bingo!")
            login_info = 1
            break
    else:
        print("You name or password is errer!")
        i += 1
    f.close()
else:
    if i == 3 and login_info == 0:
        f = open(lock, "a")
        f.write(name + "\n")
        f.close()
        print('\033[32:1m用户 %s 已经被锁定\033[0m' % name)
