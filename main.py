runner = True
bal = 50000

def withdraw():
    global bal
    amount = int(input("Enter amount you want to withdraw: "))
    if amount <= 0:
        print("Amount can't be less than or equal to 0")
    elif amount > bal:
        print("Insufficient balance")
    else:
        bal -= amount
        print(f"₹{amount} withdrawn.")
    # print("---------------------")

def deposit():
    global bal
    amount = int(input("Enter amount you want to deposit: "))
    if amount <= 0:
        print("Amount can't be less than or equal to 0")
    else:
        bal += amount
        print(f"₹{amount} deposited.")
    # print("---------------------")

def balance():
    print(f"Your balance is ₹{bal}")
    # print("---------------------")

def run():
    global runner
    print("---------------------")
    print("      LMAO BANK      ")
    print("---------------------")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")
    inputt = input("Enter your choice (1-4): ")
    if inputt == "1":
        withdraw()
    elif inputt == "2":
        deposit()
    elif inputt == "3":
        balance()
    elif inputt == "4":
        runner = False
        print("Thank you for using LMAO Bank.")
    else:
        print("Invalid input")
    # print("---------------------")

while runner:
    run()
