name = input("What's your name? \n--> ")
gender = input("Male or Female? \n--> ")
if gender == "Male":
	gender = "Mr."
elif gender == "Female":
	gender = "Ms."
age = int(input("Enter owner age: \n--> "))
rev = float(input("Enter monthly revenue: \n--> "))
cs = int(input("Enter credit score: \n--> "))
years = float(input("Your years in business: \n--> "))
has_defaults = bool(eval(input("Do you have defaults (True or False): \n-->")))
collateral_name = str(input("Enter your collateral name: \n--> "))
collateral_value = float(input("Your collateral value: \n--> "))

max_loan = 0
fee_rate = 0
final_fee = 0

if age >= 21 and years >= 2.0 and has_defaults == False:
	#tier 1
	if cs >= 720:
		max_loan = 3 * rev
		if rev >= 50000:
			fee_rate = 0.015
		else:
			fee_rate = 0.025
		#collateral and modulus fee rules
		if collateral_value >= max_loan:
			base_fee = max_loan * fee_rate
			final_fee = base_fee
			if int(collateral_value) % 5000 != 0:
				final_fee += 250
			print("Approved")
			print(f"Your max loan is: {max_loan}")
			print(f"Your base fee rate is: {fee_rate}% ")
			print(f"Your base fee is: {base_fee} ")
			print(f"Your Final Processing Fee: {final_fee}%")
			print(f"Thank you for using our machine {gender} {name} ")
	#tier 2
	elif cs >= 620 and cs < 720:
		max_loan = 1.5 * rev
		if years >= 5.0:
			fee_rate = 0.02
		else:
			fee_rate = 0.035
		if collateral_value >= max_loan:
			base_fee = max_loan * fee_rate
			final_fee = base_fee
			if int(collateral_value) % 5000 != 0:
				final_fee += 250
			print("Approved")
			print(f"Your max loan is: {max_loan}")
			print(f"Your base fee rate is: {fee_rate}% ")
			print(f"Your base fee is: {base_fee} ")
			print(f"Your Final Processing Fee: {final_fee}%")
			print(f"Thank you for using our machine {gender} {name} ")
		
	#tier 3
	elif cs < 620:
		print("Sorry your credit score is too low")
		print("Thank you for using our software {gender} {name} ")


else:
	print("Rejected: Your are not eligible for applying for loan sorry {gender} {name}")
