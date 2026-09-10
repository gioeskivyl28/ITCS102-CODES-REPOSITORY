#Problem: Global freight calculator

sender = str(input("Sender name: "))
item = str(input("Type of item:"))
isFragile = bool(input("Mahuna?"))
weight = float(input("weight of the item:"))
distance = float(input("How far in km?"))
is_express = bool(input("Is express?"))
is_international = bool(input("Is international?"))

base_cost = (weight * 2.50) + (distance * 0.15)
	
print(base_cost)

if weight <= 2.0 and distance <= 100:
	print("Free shipping")

else:
	print("with shipping fee")

total = (base_cost * 1.40) 
total1 = (total + 50)