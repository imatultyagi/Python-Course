# This program calculates the electricity bill based on the number of units consumed and whether the consumer is a senior citizen, applying different rates and a discount for senior citizens.

units = float(input("Enter the number of units consumed: "))
#Units validation
if units < 0:
    print("Invalid number of units. Please enter a positive value.")
    exit(0)
is_senior_citizen = input("Are you a senior citizen? (yes/no): ").lower()
#Senior citizen validation
if is_senior_citizen not in ["yes", "no"]:
    print("Invalid input for senior citizen. Please enter yes or no.")
    exit(0)
#Bill calculation
if units <= 100:
    bill = units * 5
elif units > 100 and units <= 300:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 200 * 7 + (units - 300) * 10
if is_senior_citizen == "yes":
    bill *= 0.9
print(f"The total electricity bill is: ₹{bill:.2f}")

