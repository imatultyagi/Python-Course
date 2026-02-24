# Problem 32

n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

# Sample Output:
# Enter number: 5
# Factorial = 120