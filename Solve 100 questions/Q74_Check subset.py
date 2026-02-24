# Problem 74

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

if set1.issubset(set2):
    print("Set1 is subset of Set2")
else:
    print("Set1 is not subset of Set2")

# Sample Output:
# Enter first set elements: 1 2
# Enter second set elements: 1 2 3 4
# Set1 is subset of Set2