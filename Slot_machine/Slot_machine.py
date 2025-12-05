#simple slot machine program
import random, time

#__________Spin the row__________
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    
    return [random.choice(symbols) for _ in range(3)]

#__________Print the outcome__________
def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

#__________Handels rewards/payouts__________
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        else:
            return bet * 20
    return 0

#__________Main function__________
def main():
    balance = 100

    print("*************************")
    print(" Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Enter your bet amount: $")

        if not bet.isdigit():
            print(f"{bet} is not a valid digit", "Please enter a valid digit", sep="\n")
            continue
        
        bet = int(bet)

        if bet > balance:
            print(f"Your balance is Insufficient for amount ${bet}!")
            continue
        
        if bet <= 0:
            print("Bet needs to be more than $0!")
            continue
        
        balance -= bet
        print("Spinning...\n")
        time.sleep(1)
        
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("You lost this bet!")

        balance += payout

    #Final message
    print("Your blanace has reached $0")
    print("Thank you for playing!")
    print("***********************")

if __name__ == "__main__":
    main()
