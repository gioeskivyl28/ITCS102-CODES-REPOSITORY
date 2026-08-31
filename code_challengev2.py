money = 4372
print("Withdraw amount:", money)

#Thousand
thou= int(money/1000)
print("1000 =", thou)
th = money%1000

#five hundred
five= int(thou/500)
print("500 =", five)
five= money%500

#two hundred
two= int(five/200)
print("200 =", two)
tw = money%200

#one hundred
one= int(tw/100)
print("100 =", one)
on= money%100

#fifty
fif = int(on/50)
print("50 =", fif)
ft = money%50

#twenty
twe = int(ft/20)
print("20 =", twe)
tn = money%20

#ten
ten = int(tn/10)
print("10 =", ten)
te = money%10

#fives
fiv = int(te/5)
print("5 =", fiv)
f = money%5

#piso
one = int(f/1)
print("1 =", one)
ps = money%1