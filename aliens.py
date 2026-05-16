
alien_colors = input("Which aliens shot down? (green, red, yellow)")

if alien_colors.lower() == "green":
	print("You earned 5 points!")

elif alien_colors.lower() == "yellow":
	print("You earned 10 points!")

else:
	print("You earned 15 points!")
