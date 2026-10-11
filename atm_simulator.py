# Week 3 Assignment: Simple ATM Simulator
# Language: Python 3


def check_balance(balance):
    print(f"\n💵 Current Balance: ₹{balance:.2f}")


def deposit_money(balance):
    try:
        amount = float(input("\nEnter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"✅ Successfully deposited ₹{amount:.2f}.")
            print(f"💵 Current Balance: ₹{balance:.2f}")
        else:
            print("⚠️ Invalid amount. Please enter a positive value.")
    except ValueError:
        print("⚠️ Please enter valid numbers only.")
    return balance


def withdraw_money(balance):
    try:
        amount = float(input("\nEnter amount to withdraw: ₹"))
        if amount <= 0:
            print("⚠️ Invalid amount.")
        elif amount > balance:
            print("❌ Insufficient balance! Transaction failed.")
        else:
            balance -= amount
            print(f"✅ Successfully withdrew ₹{amount:.2f}.")
            print(f"💵 Remaining Balance: ₹{balance:.2f}")
    except ValueError:
        print("⚠️ Please enter valid numbers only.")
    return balance


def main():
    user_pin = "1234"
    balance = 1000.00
    attempts = 3
    authenticated = False

    print("=" * 40)
    print("      WELCOME TO PYTHON ATM SYSTEM")
    print("=" * 40)

    while attempts > 0:
        entered_pin = input("\nEnter your 4-digit PIN: ")
        if entered_pin == user_pin:
            authenticated = True
            print("\n✅ PIN Verification Successful!")
            break
        else:
            attempts -= 1
            print(f"❌ Incorrect PIN! Remaining attempts: {attempts}")

    if not authenticated:
        print("\n🔒 Your account has been temporarily blocked. Please take your card.")
        return

    while True:
        print("\n-----------------------------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("-----------------------------")

        choice = input("Choose your option (1-4): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit_money(balance)
        elif choice == "3":
            balance = withdraw_money(balance)
        elif choice == "4":
            print(
                "\n🙏 Thank you for using Python ATM. Have a great day!"
            )
            break
        else:
            print("⚠️ Invalid option! Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
  
