#Problem: Global freight calculator
print("------------------------------------------------------------------------")
print("\n\t\t\tSeller Delivery Tool\n")
print("------------------------------------------------------------------------")
sender = str(input("\nWhat's the sender's name?\n --> "))
print("------------------------------------------------------------------------")
item = str(input("\nWhat type of item?\n --> "))
print("------------------------------------------------------------------------")
is_fragile = bool(eval(input("\nIs it fragile?(True of False)\n --> ")))
print("------------------------------------------------------------------------")
weight = float(input("\nWeight of the item (in kg):\n --> "))
print("------------------------------------------------------------------------")
distance = float(input("\nHow far in km?\n --> "))
print("------------------------------------------------------------------------")
is_express = bool(eval(input("\nIs it express?(True or False)\n --> ")))
print("------------------------------------------------------------------------")
is_international = bool(eval(input("\nIs it international?(True or False)\n --> ")))
print("------------------------------------------------------------------------")

print("----------------------------Delivery Type-------------------------------\n")
#Base cost Calculation
base_cost = (weight * 2.50) + (distance * 0.15)

#Free shipping

if weight <= 2.0 and distance <= 100 and is_express == False and is_international == False:
	print("\t\t\tFree shipping, no fee")
	Total = 0

#International Express
elif is_international == True and is_express == True:
	print("\t\tPackage being international is applied")
	Total = (base_cost * 1.4) + 50

#Express or Heavy International
elif is_express == True or (is_international == True and weight > 20):
	print("\tPackage being Express or Heavy International is applied.")
	Total = (base_cost * 1.2) + 25

#Oversized
elif weight > 30 or distance > 1000:
	print("\t\t     Oversized is being applied")
	Total = (base_cost + 30)

#Standard Rate
else:
	Total = base_cost
	print("Standard rate only")
print("\n ")

print("\t\t\t------RECEIPT------")
print("Name of the sender -->", sender)
print("Type of product ----->", item)
print("Total amount -------->₱", Total)
print("\t\t\tHappy Selling Mr./Ms.\n\t\t\t\t", sender)