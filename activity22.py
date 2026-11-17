Movie_Type = ["action", "comedy", "horror", "romance"]
Movie_list = []

while True:
    ans = input("Do you know any movie? (yes/no) ")

    if ans . lower() == "yes":
        print("What it its type? Select from the list:")
        for x in Movie_Type:
            print(x)

            m_type = input("Movie_Type: ")

            title = input("What is the title of the movie? ")
            Movie_list . append(title)
            print("Movie added successfully!")

    else:
        print("Thank you")
        print("Your movie list:", Movie_Type)
        