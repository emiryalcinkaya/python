grade = int(input("Enter your grade: "))

if grade < 0 or grade > 100:
	print("Invalid grade!")

elif grade <= 59:
	print("Grade: F")

elif grade <= 69:
	print("Grade: D")

elif grade <= 79:
	print("Grade: C")

elif grade <= 89: 
	print("Grade: B")

else:
	print("Grade: A")
