# Problem 63

lst = list(map(int, input("Enter elements: ").split()))
total = 0

for num in lst:
    total += num

average = total / len(lst)
print("Average =", average)

# Sample Output:
# Enter elements: 2 4 6 8
# Average = 5.0