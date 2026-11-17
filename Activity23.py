Action = []
Comedy = []
Romance = []
Horror = []
Drama = []
Adventure = []

while True:
    ask = input("Do you watch movies?  yes or no --> ").lower()
    
    if ask == "yes":
        print("These are the list of movie genre:\n1 - Action\n2 - Comedy\n3 - Romance\n4 - Horror\n5 - Drama\n6 - Adventure ")
        mg = input("What kind of genre? ")
        
        if mg == "1":
            action_choice = input("Do you want to (add) or (remove) a movie? ").lower()
            if action_choice == "add":
                mn = input("Whats the title of the movie? ").title()
                Action.append(mn)
            elif action_choice == "remove":
                mn = input("Whats the title of the movie to remove? ").title()
                if mn in Action:
                    Action.remove(mn)
                    print(f"'{mn}' has been removed.")
                else:
                    print("Movie not found in this genre.")
            else:
                print("Invalid option.")
                
            print("These are your movies under your chosen Genre: ")
            print(Action)
            
            again = input("Do you want to do it again? (yes/no): ").lower()
            if again == "yes":
                continue
            else:
                break
                
        elif mg == "2":
            action_choice = input("Do you want to (add) or (remove) a movie? ").lower()
            if action_choice == "add":
                mn = input("Whats the title of the movie? ").title()
                Comedy.append(mn)
            elif action_choice == "remove":
                mn = input("Whats the title of the movie to remove? ").title()
                if mn in Comedy:
                    Comedy.remove(mn)
                    print(f"'{mn}' has been removed.")
                else:
                    print("Movie not found in this genre.")
            else:
                print("Invalid option.")
                
            print("These are your movies under your chosen Genre: ")
            print(Comedy)
            
            again = input("Do you want to do it again? (yes/no): ").lower()
            if again == "yes":
                continue
            else:
                break
                
        elif mg == "3":
            action_choice = input("Do you want to (add) or (remove) a movie? ").lower()
            if action_choice == "add":
                mn = input("Whats the title of the movie? ").title()
                Romance.append(mn)
            elif action_choice == "remove":
                mn = input("Whats the title of the movie to remove? ").title()
                if mn in Romance:
                    Romance.remove(mn)
                    print(f"'{mn}' has been removed.")
                else:
                    print("Movie not found in this genre.")
            else:
                print("Invalid option.")
                
            print("These are your movies under your chosen Genre: ")
            print(Romance)
            
            again = input("Do you want to do it again? (yes/no): ").lower()
            if again == "yes":
                continue
            else:
                break
                
        elif mg == "4":
            action_choice = input("Do you want to (add) or (remove) a movie? ").lower()
            if action_choice == "add":
                mn = input("Whats the title of the movie? ").title()
                Horror.append(mn)
            elif action_choice == "remove":
                mn = input("Whats the title of the movie to remove? ").title()
                if mn in Horror:
                    Horror.remove(mn)
                    print(f"'{mn}' has been removed.")
                else:
                    print("Movie not found in this genre.")
            else:
                print("Invalid option.")
                
            print("These are your movies under your chosen Genre: ")
            print(Horror)
            
            again = input("Do you want to do it again? (yes/no): ").lower()
            if again == "yes":
                continue
            else:
                break
                
        elif mg == "5":
            action_choice = input("Do you want to (add) or (remove) a movie? ").lower()
            if action_choice == "add":
                mn = input("Whats the title of the movie? ").title()
                Drama.append(mn)
            elif action_choice == "remove":
                mn = input("Whats the title of the movie to remove? ").title()
                if mn in Drama:
                    Drama.remove(mn)
                    print(f"'{mn}' has been removed.")
                else:
                    print("Movie not found in this genre.")
            else:
                print("Invalid option.")
                
            print("These are your movies under your chosen Genre: ")
            print(Drama)
            
            again = input("Do you want to do it again? (yes/no): ").lower()
            if again == "yes":
                continue
            else:
                break
                
        elif mg == "6":
            action_choice = input("Do you want to (add) or (remove) a movie? ").lower()
            if action_choice == "add":
                mn = input("Whats the title of the movie? ").title()
                Adventure.append(mn)
            elif action_choice == "remove":
                mn = input("Whats the title of the movie to remove? ").title()
                if mn in Adventure:
                    Adventure.remove(mn)
                    print(f"'{mn}' has been removed.")
                else:
                    print("Movie not found in this genre.")
            else:
                print("Invalid option.")
                
            print("These are your movies under your chosen Genre: ")
            print(Adventure)
            
            again = input("Do you want to do it again? (yes/no): ").lower()
            if again == "yes":
                continue
            else:
                break
                
        else:
            print("Invalid genre choice, please try again.")
            continue
            
    elif ask == "no":
        print("Goodbye!")
        break
    else:
        print("Invalid input/ answer, please try again ")
        continue
