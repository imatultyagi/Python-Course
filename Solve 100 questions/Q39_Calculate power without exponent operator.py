# Problem 39

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1

for _ in range(exp):
    result *= base

print("Power =", result)

# Sample Output:
# Enter base: 2
# Enter exponent: 3
# Power = 8