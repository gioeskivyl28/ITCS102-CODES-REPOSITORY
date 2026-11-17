passengers = ["Ana", "Ben", "Carla"]
total = 0

while true:
    print("\n=== JEEPNEY SIMULATOR ===")
    print("1.  passenger boards")
    print("2.  Priority seat")
    print("3.  passenger seats off (by name)")
    print("4.  last passenger gets off")
    print("5.  First passenger gets off")
    print("6.  Count passengers")
    print("7.  return trip (reverse)")
    print("8.  break")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("name: ")
        passengers . append(name)
        print(name, "boarded the jeepney. ")

    elif choice == "2":
        name = input("name: ")
        passengers. remove(name)
        print(name, "got the priority seat . ")
    
   



