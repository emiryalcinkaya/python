password = "12345"
tries = 0

while tries < 3:
	entered_password = input("Password:")

	if entered_password == password:
		print("Phone Unlocked")
		break	

	else: 
		print("Wrong Password!")
		tries += 1

if tries == 3:
	print("Phone Locked For Security!!!")

