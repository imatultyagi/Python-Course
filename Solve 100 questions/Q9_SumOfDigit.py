# Problem 9

num = int(input("Enter number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits:", sum_digits)

# Sample Output:
# Enter number: 123
# Sum of digits: 6
