# Problem 85

d = {}
n = int(input("Enter number of items: "))

for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

total = 0
for value in d.values():
    total += value

print("Sum of values:", total)

# Sample Output:
# Enter number of items: 2
# Enter key: A
# Enter value: 10
# Enter key: B
# Enter value: 20
# Sum of values: 30