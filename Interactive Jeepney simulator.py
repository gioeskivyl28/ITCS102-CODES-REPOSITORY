#Interactive Jeepney simulator
route = ["Terminal", "Perez Park", "Pacific Mall"]
passengers = []
seats = 6
fare = 13
total = 0

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers), "of", seats, "seats")
    print("1 - Sakay\n2 - Priority seat\n3 - Para po !\n4 - Baba sa pinto\n5 - Baba sa harap\n6 - Seat check\n7 - Balikan\n8 - Exit")
    choice = input("Pumili: ")
    if choice == "1":
        if len(passengers) == seats:
            print("Puno na po")
        else:
            name = input("Your name? ").title()
            passengers.append(name)
            total += fare
            print(f"{name}, took at the back.")
    elif choice == "2":
        if len(passengers) == seats:
            print("Puno na po")
        else:
            name = input("Your name? ").title()
            passengers.append(name)
            total += fare
            print(f"{name}, took the priority seat.")
    elif choice == "3":
        name = input("Sinong bababa na? ").title()
        if name in passengers:
            passengers.remove(name)
            print(f"Si {name} ay bumaba na, babay ")
        else:
            print("Baka multo yarn")
    elif choice == "4":
        if len(passengers) == 0:
            print("The jeep is empty. ")
        else:
            left = passengers.pop()
            print(f"Si {left} ay bumaba na sa may pintuan.")
    elif choice == "5":
        if len(passengers) == 0:
            print("The jeep is empty. ")
        else:
            front = passengers.pop(0)
            print(f"Si {front} ay bumaba na")
    elif choice == "6":
        for i in range(len(passengers)):
            print("Seats", i + 1, passengers[i])
    elif choice == "7":
        route.reverse()
        print("route", route)
    elif choice == "8":
        print("Total fare today:", total)
    else:
        print("Invalid choice")