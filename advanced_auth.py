users_data = {}

# Register function
def register():
	username = input("Create username: ")
	password = input("Create password: ")

	# Username already exists?
	if username in users_data:
		print("This username already exists!")
	else:
		users_data[username] = password
		print("Registration succesful!")

# Login  function
def login():
	username = input("Enter username: ")
	password = input("Enter password: ")

	# Username esixts and password correct?
	if username in users_data and users_data[username] == password:
		print(f"Welcome {username}!")
	else:
		print("Wrong username or password!")

# Main program
while True:
	print("""
	1 - Register
	2 - Login 
	3 - Show users
	4 - Exit
	""")

	choice = input("Select: ")

	if choice == "1":
		register()

	elif choice == "2":
		login()

	elif choice == "3":
		print(users_data)

	elif choice == "4":
		print("Program closed.")
		break

	else:
		print("Invalid choice!")
