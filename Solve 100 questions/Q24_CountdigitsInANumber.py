# Problem 24

num = int(input("Enter number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Number of digits:", count)

# Sample Output:
# Enter number: 12345
# Number of digits: 5