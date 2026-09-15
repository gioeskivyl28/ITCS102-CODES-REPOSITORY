#rene
age = int(input("Enter your age \n-->"))
is_employed = bool(eval(input("Are you employed? (True/False) \n -->")))
credit_score = int(input("Enter your credit score: \n-->"))
annual_income = float(input("Enter your annual income \n-->"))
has_collateral = bool(eval(input("Do you have collateral? (True/False) \n-->")))

if age >= 21 and is_employed == True:
    print("You are eligible to apply for a loan")
else:
    print("Rejected: Fails baseline criteria")

if credit_score >= 750:# Tier 1
        base_rate = 5.0
        if annual_income >= 100000:
            base_rate = 4.5
        print("Loyalty discount. Final rate is:", base_rate, "%")

elif credit_score >= 600 and credit_score < 750:# Tier 2
    base_rate = 8.0
    if has_collateral == True:
            base_rate = 7.0
    elif annual_income < 40000:
            base_rate = 9.5
    print("Approved at", base_rate, "%")

else:# Tier 3 
    if credit_score < 600:
        print("Rejected: Credit score too low")
        #bituin ng mindanao
