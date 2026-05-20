users_data = {
        "emir": {
            "password": "1234",
            "balance": 5000,
            "history": []
        }
    }

# Register 
def register():

    username = input("Create username: ")
    password = input("Create password: ")

    if username in users_data:
        print("Username already exists!")

    else:
        users_data[username] = {
            "password": password,
            "balance": 0,
            "history": []
        }

        print("Registration successful!")

# Login
def login():

    username = input("Username: ")
    password = input("Password: ")

    if username in users_data and users_data[username]["password"] == password:
        print(f"Welcome {username}!")
        atm_menu(username)

    else: 
        print("Wrong username or password!")

# Show Balance
def show_balance(username):

    balance = users_data[username]["balance"]

    print(f"Your balance: {balance} EUR")

# Deposit
def deposit(username):

    amount = int(input("Deposit amount: "))

    users_data[username]["balance"] += amount

    users_data[username]["history"].append(f"Deposited {amount} EUR")

    print("Money deposited successfully!")

# Withdraw
def withdraw(username):

    amount = int(input("Withdraw amount: "))

    if amount > users_data[username]["balance"]:
        print("Insufficient balance!")

    else: 
        users_data[username]["balance"] -= amount

        users_data[username]["history"].append(f"Withdrawn {amount} EUR")

        print("Money withdrawn successfully!")

# History
def history(username):

    print("\nTransaction History:\n")

    for transaction in users_data[username]["history"]:
        print(transaction)

# ATM Menu
def atm_menu(username):

    while True:

        print("""
            1 - Show Balance
            2 - Deposit
            3 - Withdraw
            4 - History
            5 - Logout 
            """)
        
        choice = input("Select: ")

        if choice == "1":
            show_balance(username)

        elif choice == "2":
            deposit(username)

        elif choice == "3":
            withdraw(username)

        elif choice == "4":
            history(username)

        elif choice == "5":
            print("Logged out.")
            break
        
        else:
            print("Invalid choice!")

# Main Menu
while True: 

    print("""
        1 - Register
        2 - Login
        3 - Exit
        """)
    
    choice = input("Select: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Program closed.")
        break

    else: 
        print("Invalid choice!")
