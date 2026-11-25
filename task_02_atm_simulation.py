# Task 2: ATM Withdrawal Simulation

balance = 50000.0

while True:
    print("\n===== ATM MENU =====")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        print(f"Your current balance is Rs. {balance:,.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: Rs. "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        if amount <= 0:
            print("Deposit must be greater than zero.")
            continue

        balance += amount
        print(f"Deposit successful. New balance: Rs. {balance:,.2f}")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: Rs. "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        if amount <= 0:
            print("Withdrawal must be greater than zero.")
            continue

        if amount > balance:
            print("Transaction rejected. Insufficient balance.")
            continue

        balance -= amount
        print(f"Withdrawal successful. New balance: Rs. {balance:,.2f}")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 4.")
