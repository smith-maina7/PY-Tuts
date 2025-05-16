#  Exercise: Gym Membership Cost Calculator

# Write a program that calculates the cost of a gym membership based on the following rules:
# If the age is less than 0 or more than 120, print: "Invalid age"
# If the person is under 18, print: "You need to be at least 18 to register"
# If the person is 18 or older and has a discount card (has_discount_card = True):
# If they choose the premium plan (plan = "premium"), cost is Ksh 3,000
# Otherwise, cost is Ksh 1,500
# If they don’t have a discount card:
# If they choose the premium plan, cost is Ksh 5,000
# Otherwise, cost is Ksh 2,500

age = 37
has_discount_card = True
plan = "premium"

if age < 0 or age > 120:
    print("Invalid age")
elif age < 18:
    print("You need to be at least 18 to register")
elif age >= 18:
    if has_discount_card == True:
        if plan == "premium":
            print("cost is Ksh 3000")
        else:
            print("cost is Ksh 1500")
    else:
        if plan == "premium":
            print("cost is Ksh 5000")
        else:
            print("cost is Ksh 2500")
