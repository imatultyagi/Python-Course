# Problem 71

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

union_set = set1.union(set2)

print("Union:", union_set)

# Sample Output:
# Enter first set elements: 1 2 3
# Enter second set elements: 3 4 5
# Union: {1, 2, 3, 4, 5}