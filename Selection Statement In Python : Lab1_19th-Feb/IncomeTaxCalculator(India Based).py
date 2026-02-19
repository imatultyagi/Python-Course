# This program calculates the income tax based on the annual income and age of the individual, applying different tax rates and deductions for senior citizens.
income = float(input("Enter your annual income: "))
#income validation
if income < 0:
    print("Invalid income. Please enter a positive value.")
    exit(0)
#tax calculation
if income <= 250000:
    tax = 0
elif income > 250000 and income <= 500000:
    tax = (income - 250000) * 0.05
elif income > 500000 and income <= 1000000:
    tax = 12500 + (income - 500000) * 0.2
else:
    tax = 112500 + (income - 1000000) * 0.3
age = int(input("Enter your age: "))
#age validation 
if age < 0:
    print("Invalid age. Please enter a positive value.")
    exit(0)
if age >= 60:
    if income > 300000:
        tax = tax - (income - 300000) * 0.05
print(f"The total income tax you owe is: ₹{tax:.2f}")
