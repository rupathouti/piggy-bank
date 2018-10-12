import json

balance = 0
lt = 0

def deposit(amount):
    global balance
    global lt
    if(amount > 0):
        balance = balance + amount
        lt = amount

def withdraw(amount):
    global balance
    global lt
    if(balance >= amount):
        balance = balance - amount
        lt = -amount

def statement():
    print("|Statment|")
    print("Balance =",balance)
    print("Last Transaction =",lt)
   

print("Welcome to Interactive PiggyBank\n")
print("Help-")
print("Type d to Deposit")
print("Type w to Withdraw")
print("Type s to print the Statement")
print("Type h to access Help")
print("Type q to Quit\n")



action = raw_input("action> ").lower()
while(action != "q"):
    if(action == "s"):
	data=statement()
	print(data)

	
	with open('data2.txt','w') as outfile:
		json.dump(data, outfile)

    elif(action == "d"):
        print("Please Enter the value to be Deposited")
        amount = int(raw_input("deposit> "))
        deposit(amount)
    elif(action == "w"):
        print("Please Enter the value to be Withdrawn")
        amount = int(raw_input("withdraw> "))
        withdraw(amount)
    elif(action == "h"):
        print("Help-")
        print("Type d to Deposit")
        print("Type w to Withdraw")
        print("Type s to print the Statement")
        print("Type q to Quit\n")
    else:
        print("Please Enter A Correct Command")
    action = raw_input("action> ").lower();
print("Thank you for using PiggyBank...");
