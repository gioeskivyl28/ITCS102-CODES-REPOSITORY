money = int(input("Enter the amount to withdraw: "))

print("\nWithdraw amount:", money)

# Thousand
thou = money // 1000
print("1000 =", thou)
th = money % 1000

# Five hundred
five = th // 500
print("500 =", five)
fie = th % 500

# Two hundred
two = fie // 200
print("200 =", two)
tw = fie % 200

# One hundred
one = tw // 100
print("100 =", one)
on = tw % 100

# Fifty
fif = on // 50
print("50 =", fif)
ft = on % 50

# Twenty
twe = ft // 20
print("20 =", twe)
tn = ft % 20

# Ten
ten = tn // 10
print("10 =", ten)
te = tn % 10

# Five
fiv = te // 5
print("5 =", fiv)
f = te % 5

# One peso
one_peso = f // 1
print("1 =", one_peso)