# Problem 73

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

difference_set = set1.difference(set2)

print("Difference (set1 - set2):", difference_set)

# Sample Output:
# Enter first set elements: 1 2 3 4
# Enter second set elements: 3 4 5
# Difference (set1 - set2): {1, 2}