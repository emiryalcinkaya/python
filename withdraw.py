balance = 3500

withdraw = int(input("How much money do you want to withdraw? "))

if withdraw <= balance:
	print("Transaction successful!")

else:
	print("Insufficient balance!")


