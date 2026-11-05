from getpass import getpass

u = "gio"
psword = "kalachuchi25"
is_login = False

while is_login == False:
    user = input("Enter username: ").lower()
    pas = getpass("Enter your password: ")

    if user == u and pas == psword:
        print("LOGGED IN")
        is_login == True
        break
    else:
        print("LOG IN DENIED")
        is_login == False
        continue