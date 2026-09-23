#rene
age = int(input("Enter your age\n--> "))
is_employed = input("Are you employed? (yes/no)\n--> ").strip().lower() == "yes"
credit_score = int(input("Enter your credit score: \n--> "))
annual_income = float(input("Enter your annual income\n--> "))
has_collateral = input("Do you have collateral? (yes/no)\n--> ").strip().lower() == "yes"

if age >= 21 and is_employed:
    print("You are eligible to apply for a loan")

    base_rate = None

    if credit_score >= 750:
        base_rate = 5.0
        print("Tier 1. Base rate is:", base_rate, "%")
        if annual_income >= 100000:
            base_rate -= 0.5
            print("Loyalty discount applied. Final rate is:", base_rate, "%")

    elif 600 <= credit_score < 750:
        base_rate = 8.0
        print("Tier 2. Base rate is:", base_rate, "%")
        if has_collateral:
            base_rate -= 1.0
            print("Collateral discount applied. Final rate is:", base_rate, "%")
        elif annual_income < 40000:
            base_rate += 1.5
            print("Low income surcharge applied. Final rate is:", base_rate, "%")

    else:
        print("Rejected: Credit score too low")

    if base_rate is not None:
        print("Approved at", base_rate, "%")

else:
    print("Not eligible to apply for a loan (must be 21+ and employed)")

print("Thank you for using our software")

#bituin ng mindanao
