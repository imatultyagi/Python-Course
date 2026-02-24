# Problem 10

num = int(input("Enter number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

# Sample Output:
# Enter number: 1234
# Reversed number: 4321