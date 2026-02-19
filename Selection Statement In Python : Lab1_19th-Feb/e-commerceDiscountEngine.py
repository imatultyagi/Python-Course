# This program calculates the discount for a shopping cart based on the cart value, membership type, and whether it is a festival season.

cart_value = float(input("Enter the cart value: "))
#Cart value validation 
if cart_value < 0:
    print("Invalid cart value. Please enter a positive value.")
    exit(0)
membership = input("Enter your membership type (Silver/Gold/Platinum): ").lower()
#Membership validation
if membership not in ["silver", "gold", "platinum"]:
    print("Invalid membership type. Please enter Silver, Gold, or Platinum.")
    exit(0)
festival_season = input("Is it a festival season? (yes/no): ").lower()
#Festival season validation
if festival_season not in ["yes", "no"]:
    print("Invalid input for festival season. Please enter yes or no.")
    exit(0)
#Discount calculation
discount = 0    
if cart_value > 10000:
    discount += 1000
if membership == "gold":
    discount += 500
elif membership == "platinum":
    discount += 1000
if festival_season == "yes":
    discount += 200
final_price = cart_value - discount
print(f"The final price after discount is: ₹{final_price:.2f}")
