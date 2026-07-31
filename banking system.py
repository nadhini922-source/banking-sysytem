# Simple Banking System

balance = 1000

def check_balance():
    print("Current Balance: ₹", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    balance += amount
    print("Deposit Successful!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful!")
    else:
        print("Insufficient Balance!")

while True:
    print("\n===== Banking System =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using the Banking System!")
        break
    else:
        print("Invalid Choice! Please try again.")