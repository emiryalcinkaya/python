visited_place = ['Ankara', 'Istanbul', 'Amsterdam', 'Berlin', 'München', 'Antalya'] # List of the visited cities

print(len(visited_place)) # Printing len (numbers of value in con.)
print(visited_place)

message = "\nThose are my visited cities in the world."

visited_place.append("Izmir")
visited_place.append("Utrecht")
visited_place.append("Rostock") # Added new visited cities

print(message)
print(sorted(visited_place)) # Printing sorting of the visited cities from A-Z
print(len(visited_place)) # Repated printing len

message = "\nThose are my current visited cities in the world."

print(message)
print(sorted(visited_place, reverse=True)) #Printing reverse sorting of the visited cities from Z-A

