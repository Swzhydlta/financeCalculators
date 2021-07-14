# Daniel Nel
# Capstone project 1: Finance Calculators

# This program allows a user to access two different financial calculators,
# an investment calculator and a home lone repayment calculator.

import math

# Ask the user whether they want to calculate their interest or their bond.
# Change the user's selection to a lowercase word.

investment_or_bond = input('''Choose either 'investment' or 'bond' from the menu below to proceed:
Investment     - to calculate the amount of interest you'll earn on interest.
Bond           - to calculate the amount you'll have to pay on a home loan. \n''').lower()

# Check if the user chose 'investment', 'bond', or entered an invald input.
# If the user chose 'investment', save a few pieces of data as variables.
# The data points are: investment amount, interest rate, number of years to invest for, and interest type.

if investment_or_bond == "investment":
    amount = float(input("How much are you depositing? "))
    interest_rate = float(input("What is the interest rate? "))
    years = int(input("How many years will your investment be active for? "))
    interest_type = input("Is the interest simple or compound? ").lower()
    interest_percent = interest_rate / 100
    
    # If the interest type is "simple", calculate the investment.
    # Perform calclation using the 'A = amount(1 + r * years)' formula.
    
    if interest_type == "simple":
        total_investment = amount * (1 + interest_percent * years)
        print(f"In {years} years, your investment will be R", round(total_investment, 2))

    # Else if the interest type is "compounding", calculate the investment.
    # Perform calclation using the 'A = amount * math.pow((1 + r), years)' formula.

    else:
        if interest_type == "compound":
            total_investment = amount * math.pow((1 + interest_percent), years)
            print(f"In {years} years, your investment will be R", round(total_investment, 2))

# If the user chose 'bond', save a few pieces of data as variables.
# The data points are: house value, interest rate, and months over which to pay.

elif investment_or_bond == "bond":
        house_value = float(input("What is the value of your house? "))
        interest_rate = float(input("What is the interest rate? "))
        months = int(input("How many months do you have to pay the bond back? "))

        # Calculate monthly interest rate by dividing interest rate by 100 to get a percent value and then dividing that by 12
        monthly_interest = (interest_rate / 12) / 100

        # Calculate the amount the user has to pay back per month using the x=(i.P)/(1-(1+i)^(-n)) equation.
        one = 1
        monthly_repayment = (monthly_interest * house_value) / (one - (one + monthly_interest) ** (-months))
        monthly_repayment = round(monthly_repayment, 2)
        print(f"The amount you will have to pay back each month is R{monthly_repayment}")

# Catch input errors.
else:
    print("Please enter a valid choice")

    














