# Problem 22

n = int(input("Enter number: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)

# Sample Output:
# Enter number: 5
# Factorial = 120