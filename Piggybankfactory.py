# How to call function from creating an object

class Piggybank:
    pass
def PiggybankFactory():
    balance=0
    lt=0
    def deposit(amount):
        nonlocal balance
        nonlocal lt
        if(amount > 0):
            balance = balance + amount
            lt = amount

    def withdraw(amount):
        nonlocal balance
        nonlocal lt
        if(balance >= amount):
            balance = balance - amount
            lt = -amount
    def statement():
        print("Balance =",balance)
        print("Last Transaction =",lt)
    pg=Piggybank()
    pg.deposit=deposit
    pg.withdraw=withdraw
    pg.statement=statement
    return pg
pg1=PiggybankFactory()
pg1.deposit(50)
pg1.statement()
