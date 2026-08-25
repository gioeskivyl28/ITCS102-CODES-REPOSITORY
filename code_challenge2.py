#code challenge no.2
#Example bank deposit

money = 6438

print("Money to deposit -->", money)

#Money to deposit 
thousand = money//1000
money = money - thousand*1000
fivehundred = money//500
money = money - fivehundred*500
twohundred = money//200
money = money -  twohundred*200
hundred = money//100
money = money - hundred*100
fifty = money//50
money = money - fifty*50
twenty = money//20
money = money - twenty*20
ten = money//10
money = money - ten*10
five = money//5
money = money - five*5
one = money//1
money = money - one*1

print("You have ", thousand,"of ", "1k")
print("You have ", fivehundred,"of ", "500")
print("You have ", twohundred,"of ", "200")
print("You have ", hundred,"of ", "100")
print("You have ", fifty,"of ", "50")
print("You have ", twenty,"of ", "20")
print("You have ", ten,"of ", "10")
print("You have ", five,"of ", "5")
print("You have ", one,"of ", "1")

