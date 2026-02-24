# Problem 25

n = int(input("Enter N: "))
i = 1
sum_even = 0

while i <= n:
    if i % 2 == 0:
        sum_even += i
    i += 1

print("Sum of even numbers:", sum_even)

# Sample Output:
# Enter N: 10
# Sum of even numbers: 30