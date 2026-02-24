# Problem 27

n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

# Sample Output:
# Enter number of terms: 5
# 0 1 1 2 3