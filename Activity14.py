age = int(input("Enter your age \n-->"))
is_employed = bool(input("Are you employed? (True/False) \n -->"))
credit_score = int(input("Enter your credit score: \n-->"))
annual_income = float(input("Enter your annual income \n-->"))
has_collateral = bool(input("Do you have collateral? (True/False) \n-->"))

if age >= 21 and is_employed == True:
    print("You are eligible to apply for a loan.")
else:
    print("You are not eligible to apply for a loan.")
    if credit_score >= 750: #tier 1
        print("You have a high credit score")
        if annual_income >= 100000:
            base_rate = 4.5
            print("You have a high salary and high credit score your interest rate is", base_rate)
        else:
            base_rate = 5.0
            print("You have a high salary and high credit score your interest rate is", base_rate)   
    if credit_score >= 600 and credit_score < 750: #tier 2
        base_rate = 8.0
        if has_collateral == True:
            base_rate = (base_rate - 7)
            elif
            

