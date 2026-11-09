rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end = " ")
    for k in range(1, 2 * i):
        print("*", end = " ")
    print()
   
for l in range(rows - 1, 0, -1):
    for m in range(rows - l):
        print(" ", end = " ")
    for m in range(1, 2 * l):
        print("*", end = " ")
    print()