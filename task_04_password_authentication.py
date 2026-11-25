# Task 4: Password Authentication System

correct_username = "admin"
correct_password = "12345"
max_attempts = 3
logged_in = False

for attempt in range(1, max_attempts + 1):
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty.")
    elif username == correct_username and password == correct_password:
        print("Login successful. Welcome!")
        logged_in = True
        break
    else:
        print("Incorrect username or password.")

    remaining = max_attempts - attempt
    if remaining > 0:
        print(f"Attempts remaining: {remaining}")

if not logged_in:
    print("Account locked after three failed login attempts.")
