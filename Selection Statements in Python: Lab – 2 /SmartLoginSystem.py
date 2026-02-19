# This program simulates a simple login system where the user has three attempts to enter the correct username and password. If the user fails to log in after three attempts, the account is locked.

predefined_username = "user123"
predefined_password = "pass456"
# Login attempts counter
attempts = 0
while attempts < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Username validation
    if username != predefined_username:
        print("Invalid username. Please try again.")
        attempts += 1
        continue
    # Password validation
    if password != predefined_password:
        print("Invalid password. Please try again.")
        attempts += 1
        continue
    # Successful login
    print("Login successful!")
    break
if attempts == 3:
    print("Account locked due to too many failed attempts.")
