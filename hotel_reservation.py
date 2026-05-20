rooms = [
        {"room_number": "1", "price": 50, "capacity": 1, "is_available": True},
        {"room_number": "2", "price": 100, "capacity": 2, "is_available": True},  
        {"room_number": "3", "price": 100, "capacity": 2, "is_available": False},
        {"room_number": "4", "price": 150, "capacity": 3, "is_available": True},        
        ] # Rooms list

reservation_history = []

def view_available_rooms(): # View available rooms list
    print("Available rooms: ")

    for room in rooms:
        if room["is_available"]:
            print(f"Room {room['room_number']}, Price {room['price']}, Capacity {room['capacity']}")

def make_reservation(): # Make a reservation
    room_number = input("Enter room number: ")
    found = False

    for room in rooms:

            if room["room_number"] == room_number:
                
                found = True

                if room["is_available"]:
                    room["is_available"] = False
                    reservation = "Room number "+ room_number + " is reserved."
                    reservation_history.append(reservation) # Adding reservation history
                    print(reservation)
                else: 
                    print("Room not available")
                
                break

    if not found:
        print("Invalid number")

def cancel_reservation(): # Cancel a reservation
    room_number = input("Enter room number: ")
    found = False 

    for room in rooms:

            if room["room_number"] == room_number:
                
                found = True

                if not room["is_available"]:
                    room["is_available"] = True
                    cancelation = "Room number "+ room_number + " canceled."
                    reservation_history.append(cancelation) # Adding reservation history
                    print(cancelation)
                else: 
                    print("Room not available")
                
                break
            
    if not found:
        print("Invalid number")

def get_reservation_history():
    print(reservation_history)

# Menu 

while True:

    print("""
        1 - View Available Rooms
        2 - Make Reservations
        3 - See Reservation History
        4 - Cancel Reservations
        5 - Exit
        """)
    
    choice = input("Select: ")

    if choice == "1":
        view_available_rooms()
    
    elif choice == "2":
        make_reservation()

    elif choice == "3":
        get_reservation_history()

    elif choice == "4":
        cancel_reservation()

    elif choice == "5":
        print("exit")
        break

    else: 
        print("Invalid number")

