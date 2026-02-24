# Problem 30

total = 0

while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    total += num

print("Total sum =", total)

# Sample Output:
# Enter number (0 to stop): 5
# Enter number (0 to stop): 10
# Enter number (0 to stop): 0
# Total sum = 15