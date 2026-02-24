# Problem 5

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest =", ci)

# Sample Output:
# Enter principal: 1000
# Enter rate: 5
# Enter time: 2
# Compound Interest = 102.5