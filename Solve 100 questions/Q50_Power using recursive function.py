# Problem 50

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Power =", power(base, exp))

# Sample Output:
# Enter base: 2
# Enter exponent: 3
# Power = 8