alien0 = {'color': 'green', 'points': 5}
alien1 = {'color': 'yellow', 'points': 10}
alien2 = {'color': 'red', 'points': 15}

alien = input("Which alien is die? ")

if alien == alien0:
	print("You earn " + str(alien0['points']) + " points!")

elif alien == alien1:
	print("You earn " + str(alien1['points']) + " points!")

else:
	print("You earn " + str(alien2['points']) + " points!")
