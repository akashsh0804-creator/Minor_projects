#simple banking program

#__________Display the current balance__________
def show_balance(balance):
    print("*******************")
    print(f"Your current balance is ${balance:.2f}")
    print("*******************")

#__________Deposition of the money__________
def deposit():
    amount = float(input("Enter an amount to be deposited: $"))

    if amount < 0:
        print("*******************")
        print(f"${amount} is a not a valid amount!")
        print("*******************")
        return 0
    else:
        print("*******************")
        print(f"${amount} successfully deposited")
        print("*******************")
        return amount

#__________Withdrawl of the money__________
def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: $"))

    if amount < 0:
        print("*******************")
        print(f"${amount} is a not a valid amount!")
        print("*******************")
        return 0
    elif amount > balance:
        print("*******************")
        print("You don't have sufficient amount to withdraw!")
        print("*******************")
        return 0
    else:
        print("*******************")
        print(f"${amount} successfully withdrawed")
        print("*******************")
        return amount

#__________Main function__________
def main():
    balance = 0
    is_running = True

#taking user input for an operation
    while is_running:
        print("*******************")
        print("  Banking program  ")
        print("*******************")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("*******************")

        choice = int(input("Enter your choice (1-4):"))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance) 
        elif choice == 4:
            is_running = False
        else :
            print("*******************")
            print(f"{choice} is an INVALID choice!")
            print("*******************")

    print("*******************")
    print("Thank you! Have a nice day!")
    print("*******************")

if __name__ == "__main__":
    main()
