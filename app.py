from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
#Prompt the user to register with their name and PIN number.

print("          === Automated Teller Machine ===          ")
name = input("Enter name to register:")
pin = input("Enter PIN:")
while True:
    if len(name) > 10:
        print("The maximum name length is 10 characters")
        name = input("Enter name to register:")
        pin = input("Enter PIN:")
    elif len(pin) > 4:
        print("PIN must contain 4 numbers")
    else:
        break
    
balance = 0
print(name + " has been registered with a balance of $"+ str(balance))

#Prompt the user to log in, and display menu options upon valid login.

while True:
    name_to_validate = input("Enter name:")
    pin_to_validate = input("Enter PIN:")
    if(name_to_validate == name and pin_to_validate == pin):
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
while True:
    atm_menu(name)
    option = input("Choose an option:")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    else:
        account.logout(name)
        break




