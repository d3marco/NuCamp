def show_balance(balance):
    print(float(balance))


def deposit(balance):
    amount = input("Enter amount to deposit:")
    return float(balance)+float(amount)


def withdraw(balance):
    amount = input("Enter amount to withdraw:")
    if float(amount) > float(balance):
        print("Where are you going to get that kind of money?")
    return float(balance)-float(amount)


def logout(name):
    print("Goodbye "+name+"!")
