# Problem 45

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input("Enter number: "))
print("Sum of digits =", sum_digits(num))

# Sample Output:
# Enter number: 123
# Sum of digits = 6