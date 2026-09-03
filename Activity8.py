#concatenation = combining of strings

name = input("What is your name?")
hobbies = ""

h = input("Anong mga pautot mo? --> ")
hobbies += h + ", "

h = input("Ay jejemon, ano pa ngani? ")
hobbies += h + ", "

h = input("Amazing ka boii, meron pa?")
hobbies += h + ", "

h = input("Yari ka sa mama mo nyan, ano pa? ")
hobbies += h + ", "

print("So, ang mga pautot ni", name," ay", hobbies)