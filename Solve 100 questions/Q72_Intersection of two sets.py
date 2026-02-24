# Problem 72

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

intersection_set = set1.intersection(set2)

print("Intersection:", intersection_set)

# Sample Output:
# Enter first set elements: 1 2 3
# Enter second set elements: 2 3 4
# Intersection: {2, 3}