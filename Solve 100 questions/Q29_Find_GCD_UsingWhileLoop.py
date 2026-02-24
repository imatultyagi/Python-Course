# Problem 29

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)

# Sample Output:
# Enter first number: 12
# Enter second number: 18
# GCD = 6