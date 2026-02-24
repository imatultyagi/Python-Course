# Problem 36

n = int(input("Enter number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

# Sample Output:
# Enter number: 6
# 1 2 3 6