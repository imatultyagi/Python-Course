# Problem 75

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

sym_diff = set1.symmetric_difference(set2)

print("Symmetric Difference:", sym_diff)

# Sample Output:
# Enter first set elements: 1 2 3
# Enter second set elements: 3 4 5
# Symmetric Difference: {1, 2, 4, 5}