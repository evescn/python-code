def cash_money(amount):
    while amount > 0:
        amount -= 100
        print("又来取钱了")
        yield 100
        # print("又来取钱了")


atm = cash_money(500)
print(type(atm))
print("取走了", next(atm))
print("取走了", next(atm))
print("取走了", next(atm))
print("取走了", next(atm))
print("取走了", next(atm))

g = (x * x for x in range(10))

for i in g:
    print(i)