# Problem 62

lst = list(map(int, input("Enter elements: ").split()))
total = 0

for num in lst:
    total += num

print("Sum =", total)

# Sample Output:
# Enter elements: 1 2 3 4
# Sum = 10