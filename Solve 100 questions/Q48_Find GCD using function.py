# Problem 48

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD =", gcd(a, b))

# Sample Output:
# Enter first number: 12
# Enter second number: 18
# GCD = 6