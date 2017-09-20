def cash_money(amount):
    while amount > 0:
        amount -= 100
        print("又来取钱了")
        yield 100
        # print("又来取钱了")


atm = cash_money(500)
print(type(atm))
print(next(atm))
print(next(atm))
print(next(atm))
print(next(atm))
print(next(atm))
