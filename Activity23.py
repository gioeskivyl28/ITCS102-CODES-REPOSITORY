Bruno_mars = []
Charlie_puth = []
while True:
    ask = input("Do you listen to music? yes/no ").lower()
    if ask == "yes":
        print("List of Music Artists:\n1 - Bruno Mars\n2 - Charlie Puth")
        mus = input("Who among them youve chosen? ")
        if mus == "1":
            print("Bruno Mars selected")
            op = input("Are you going to add a music or remove? add or remove ").lower()
            if op == "add":
                m = input("What music would yoy add? ").title()
                Bruno_mars.append(m)
                print("These are your songs")
                print(Bruno_mars)
                again = input("Would you like to Try agaim? yes or no ").lower()
                
                if again == "yes":
                    continue
                else:
                    break
            elif op == "remove":
                print(Bruno_mars)
                rem = input("Which song would you like to remove? ").title()
                Bruno_mars.remove(rem)
                print("List of songs: ")
                print(Bruno_mars)
                again = input("Would you like to Try again? yes or no ").lower()
                
                if again == "yes":
                    continue
                else:
                    break
        elif mus == "2":
            print("Charlie Puth selected")
            op = input("Are you going to add a music or remove? add or remove").lower()
            if op == "add":
                m = input("What music would you add? ").title()
                Charlie_puth.append(m)
                print("These are your songs")
                print(Charlie_puth)
                again = input("Would you like to Try again? yes or no ").lower()
                
                if again == "yes":
                    continue
                else:
                    break
            elif op == "remove":
                print(Charlie_puth)
                rem = input("Which song would you like to remove? ").title()
                Charlie_puth.remove(rem)
                print("List of songs: ")
                print(Charlie_puth)
                again = input("Would you like to Try again? yes or no ").lower()
                
                if again == "yes":
                    continue
                else:
                    break
            
    else:
            print("babye")
            break
                
    
