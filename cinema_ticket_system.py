
age = int(input("Enter your age: "))

status = input("Are you a student? ")

if age < 12: 
	price = 5

elif age <= 24: 
	price = 10

else:
	price = 15

if status == "yes":
	price = price - 3

if price < 0:
	price = 0

print("Your ticket price is:", price, "€")
